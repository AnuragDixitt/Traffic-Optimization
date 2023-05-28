from flow.scenarios.loop import LoopScenario
from flow.core.experiment import Experiment
from flow.core.params import VehicleParams
from flow.controllers.car_following_models import IDMController
from flow.controllers.routing_controllers import ContinuousRouter
from flow.scenarios.loop import ADDITIONAL_NET_PARAMS
from flow.core.params import NetParams
from flow.core.params import InitialConfig
from flow.core.params import TrafficLightParams
from flow.envs.loop.loop_accel import AccelEnv
from flow.core.params import SumoParams
from flow.envs.loop.loop_accel import ADDITIONAL_ENV_PARAMS
from flow.core.params import EnvParams

name = "ring_example"

vehicles = VehicleParams()
vehicles.add(
    veh_id="human",
    acceleration_controller=(IDMController, {}),
    routing_controller=(ContinuousRouter, {}),
    num_vehicles=22
)

print(ADDITIONAL_NET_PARAMS)

net_params = NetParams(additional_params=ADDITIONAL_NET_PARAMS)

initial_config = InitialConfig(spacing="uniform", perturbation=1)

traffic_lights = TrafficLightParams()

sumo_params = SumoParams(sim_step=0.1, render=True)

print(ADDITIONAL_ENV_PARAMS)

env_params = EnvParams(additional_params=ADDITIONAL_ENV_PARAMS)

scenario = LoopScenario(
    name="ring_example",
    vehicles=vehicles,
    net_params=net_params,
    initial_config=initial_config,
   traffic_lights=traffic_lights
)

env = AccelEnv(env_params=env_params, sumo_params=sumo_params, scenario=scenario)

exp = Experiment(env=env)

_ = exp.run(num_runs=1, num_steps=3000)