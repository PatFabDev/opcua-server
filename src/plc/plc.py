from plc.io import MixerTankIO
from plant.mixing_tank.mixing_tank import MixingTankPhase


class PLC:
    def __init__(self, io: MixerTankIO):
        self.io = io

    def get_status(self) -> dict:
        return self.io.get_status()

    def update(self) -> None:
        phase = self.io.get_phase()

        if phase == MixingTankPhase.IDLE:
            self._handle_idle()

        elif phase == MixingTankPhase.FILLING_1:
            self._handle_filling_1()

        elif phase == MixingTankPhase.FILLING_2:
            self._handle_filling_2()

        elif phase == MixingTankPhase.HEATING:
            self._handle_heating()

        elif phase == MixingTankPhase.COOLING:
            self._handle_cooling()

        elif phase == MixingTankPhase.DRAINING:
            self._handle_draining()

    def _handle_idle(self) -> None:
        self.io.set_phase(MixingTankPhase.FILLING_1)

    def _handle_filling_1(self) -> None:
        target_level = self.io.get_capacity() * 0.70

        if self.io.get_level() < target_level:
            self.io.open_inlet_valve_1()
        else:
            self.io.close_inlet_valve_1()
            self.io.set_phase(MixingTankPhase.FILLING_2)

    def _handle_filling_2(self) -> None:
        target_level = self.io.get_capacity()

        if self.io.get_level() < target_level:
            self.io.open_inlet_valve_2()
        else:
            self.io.close_inlet_valve_2()
            self.io.set_phase(MixingTankPhase.HEATING)

    def _handle_heating(self) -> None:
        self.io.turn_heater_on()
        self.io.start_agitator()

        if self.io.get_temperature() >= 70.0:
            self.io.turn_heater_off()
            self.io.set_phase(MixingTankPhase.COOLING)

    def _handle_cooling(self) -> None:
        if self.io.get_temperature() > 30.0:
            self.io.start_agitator()
        else:
            self.io.stop_agitator()
            self.io.open_outlet_valve()
            self.io.set_phase(MixingTankPhase.DRAINING)

    def _handle_draining(self) -> None:
        if self.io.get_level() > 0.0:
            self.io.open_outlet_valve()
        else:
            self.io.close_outlet_valve()
            self.io.set_phase(MixingTankPhase.IDLE)