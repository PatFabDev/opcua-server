from plant.plant import Plant
from plant.mixing_tank.mixing_tank import MixerTank


class SimulationEngine:
    def __init__(
        self,
        plant: Plant,
        inlet_flow_rate_1: float = 20.0,
        inlet_flow_rate_2: float = 15.0,
        outlet_flow_rate: float = 15.0,
        heating_rate: float = 2.0,
        cooling_rate: float = 1.0,
        ambient_temperature: float = 25.0,
    ):
        self.plant = plant

        self.inlet_flow_rate_1 = inlet_flow_rate_1
        self.inlet_flow_rate_2 = inlet_flow_rate_2
        self.outlet_flow_rate = outlet_flow_rate

        self.heating_rate = heating_rate
        self.cooling_rate = cooling_rate
        self.ambient_temperature = ambient_temperature

    def update(self, dt: float) -> None:
        for machine in self.plant.machines.values():
            if isinstance(machine, MixerTank):
                self._update_mixer_tank(machine, dt)

    def _update_mixer_tank(
        self,
        mixer_tank: MixerTank,
        dt: float,
    ) -> None:
        self._simulate_inflow(mixer_tank, dt)
        self._simulate_outflow(mixer_tank, dt)
        self._simulate_heating(mixer_tank, dt)
        self._simulate_cooling(mixer_tank, dt)

        mixer_tank.update_sensors()

    def _simulate_inflow(
        self,
        mixer_tank: MixerTank,
        dt: float,
    ) -> None:
        status = mixer_tank.get_status()

        if status["inlet_valve_1"] == "OPEN":
            mixer_tank.fill(
                self.inlet_flow_rate_1 * dt
            )

        if status["inlet_valve_2"] == "OPEN":
            mixer_tank.fill(
                self.inlet_flow_rate_2 * dt
            )

    def _simulate_outflow(
        self,
        mixer_tank: MixerTank,
        dt: float,
    ) -> None:
        status = mixer_tank.get_status()

        if status["outlet_valve"] == "OPEN":
            mixer_tank.drain(
                self.outlet_flow_rate * dt
            )

    def _simulate_heating(
        self,
        mixer_tank: MixerTank,
        dt: float,
    ) -> None:
        status = mixer_tank.get_status()

        if status["heater"] == "ON":
            mixer_tank.tank.temperature += (
                self.heating_rate * dt
            )

    def _simulate_cooling(
        self,
        mixer_tank: MixerTank,
        dt: float,
    ) -> None:
        status = mixer_tank.get_status()

        if (
            status["heater"] == "OFF"
            and mixer_tank.get_temperature() > self.ambient_temperature
        ):
            mixer_tank.tank.temperature = max(
                mixer_tank.get_temperature()
                - self.cooling_rate * dt,
                self.ambient_temperature,
            )