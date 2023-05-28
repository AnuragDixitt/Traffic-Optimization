from flow.scenarios import MergeScenario
from flow.core.params import VehicleParams
from flow.controllers import IDMController
from flow.core.params import SumoCarFollowingParams
from flow.core.params import InFlows
from flow.scenarios.merge import ADDITIONAL_NET_PARAMS
from flow.core.params import NetParams
from flow.core.params import SumoParams, EnvParams, InitialConfig
from flow.envs.loop.loop_accel import AccelEnv, ADDITIONAL_ENV_PARAMS
from flow.core.experiment import Experiment

vehicles = VehicleParams()
vehicles.add(
    veh_id="human",
    acceleration_controller=(IDMController, {}),
    car_following_params=SumoCarFollowingParams(
        speed_mode="obey_safe_speed",
    ),
    num_vehicles=20
)

inflow = InFlows()
inflow.add(
    veh_type="human",
    edge="inflow_highway",
    vehs_per_hour=2000,
    departSpeed=10,
    departLane="random"
)
inflow.add(
    veh_type="human",
    edge="inflow_merge",
    vehs_per_hour=100,
    departSpeed=10,
    departLane="random"
)

additional_net_params = ADDITIONAL_NET_PARAMS.copy()
additional_net_params["pre_merge_length"] = 500

net_params = NetParams(
    inflows=inflow,
    no_internal_links=False,
    additional_params=additional_net_params
)

sumo_params = SumoParams(render=True, sim_step=0.2)

env_params = EnvParams(additional_params=ADDITIONAL_ENV_PARAMS)

initial_config = InitialConfig()

scenario = MergeScenario(
    name="merge-example",
    vehicles=vehicles,
    net_params=net_params,
    initial_config=initial_config
)

env = AccelEnv(env_params=env_params, sumo_params=sumo_params, scenario=scenario)

exp = Experiment(env=env)

_ = exp.run(num_runs=1, num_steps=1500)