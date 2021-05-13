import os
import controlDict as cd
import clean_times

main_project_file = "./main_project"

end_time = 0.5
initial_timestep=0.1

if int(end_time/initial_timestep)!=float(end_time/initial_timestep):
    raise ValueError("the ratio of end_time to initial_timestep must be a positive integer!")

timestep_refinement_factor = 2
levels = 5
timesteps_num = [end_time/initial_timestep*timestep_refinement_factor**i for i in range(levels)]

deltaTs = [initial_timestep/timestep_refinement_factor**i for i in range(levels)]

print(timesteps_num)
print(deltaTs)


def run_case(main_project_file, level, dt):
    os.system("cp -R {} {}-{}".format(main_project_file, main_project_file, level))

    cd.set_end_time(new_end_time=end_time, case_path="./{}-{}".format(main_project_file, level))
    cd.set_timestep_size(new_timestep_size=dt, case_path="./{}-{}".format(main_project_file, level))
    cd.set_write_interval(new_write_interval=1, case_path="./{}-{}".format(main_project_file, level))

    # run the case
    os.system('cd {}-{} && ./run.sh'.format(main_project_file, level))

    # cleaning up the data
    clean_times.leave_last_time('./{}-{}'.format(main_project_file, level))

for level, dt  in zip(list(range(1,levels+1)),deltaTs):
    run_case(main_project_file,level,dt)



# cd.set_end_time(new_end_time=10, case_path="./modified-system")
# cd.set_timestep_size(new_timestep_size=0.1, case_path="./modified-system")
# cd.set_write_interval(new_write_interval=1, case_path="./modified-system")

