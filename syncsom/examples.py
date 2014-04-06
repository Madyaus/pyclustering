from syncsom import syncsom;

from samples.definitions import SIMPLE_SAMPLES;
from samples.definitions import FCPS_SAMPLES;

from support import read_sample, draw_clusters, draw_dynamics;
from support import timedcall;

def template_clustering(file, map_size, trust_order, sync_order = 0.999, show_dyn = False, show_layer1 = False, show_layer2 = False, show_clusters = True):
    # Read sample
    sample = read_sample(file);

    # Create network
    network = syncsom(sample, map_size[0], map_size[1]);
    
    # Run processing
    (ticks, (dyn_time, dyn_phase)) = timedcall(network.process, trust_order, show_dyn, sync_order);
    print("Sample: ", file, "\t\tExecution time: ", ticks, "\n");
    
    # Show dynamic of the last layer.
    if (show_dyn == True):
        draw_dynamics(dyn_time, dyn_phase, x_title = "Time", y_title = "Phase", y_lim = [0, 2 * 3.14]);
    
    if (show_clusters == True):
        clusters = network.get_som_clusters();
        draw_clusters(network.weights, clusters);
    
    # Show network stuff.
    if (show_layer1 == True):
        network.show_som_layer();
    
    if (show_layer2 == True):
        network.show_sync_layer();
    
    if (show_clusters == True):
        clusters = network.get_clusters();
        draw_clusters(sample, clusters);
  

def cluster_simple3():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, [4, 4], 3, 0.999, True, True, True, True);
    
def cluster_simple4():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, [3, 3], 3, 0.999, True, True, True);
    
def cluster_simple5():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, [3, 3], 3, 0.999, True, True, True);

def cluster_lsun():
    template_clustering(FCPS_SAMPLES.SAMPLE_LSUN, [9, 9], 10, 0.999, True, True, True);
     
def cluster_target():
    template_clustering(FCPS_SAMPLES.SAMPLE_TARGET, [9, 9], 20, 0.999, True, True, True);

def cluster_two_diamonds():
    template_clustering(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, [10, 10], 5, 0.999, True, True, True);

def cluster_wing_nut():
    template_clustering(FCPS_SAMPLES.SAMPLE_WING_NUT, [10, 10], 5, 0.999, True, True, True);

def cluster_chainlink():
    template_clustering(FCPS_SAMPLES.SAMPLE_CHAINLINK, [10, 10], 15, 0.999, True, True, True);

def cluster_hepta():
    template_clustering(FCPS_SAMPLES.SAMPLE_HEPTA, [7, 7], 5, 0.999, True, True, True);

def cluster_tetra():
    "Problem here"
    template_clustering(FCPS_SAMPLES.SAMPLE_TETRA, [7, 7], 5, 0.998, True, True, True);

def experiment_execution_time():
    template_clustering(FCPS_SAMPLES.SAMPLE_LSUN, [9, 9], 10, 0.998, False, False, False, False);
    template_clustering(FCPS_SAMPLES.SAMPLE_TARGET, [9, 9], 20, 0.998, False, False, False, False);
    template_clustering(FCPS_SAMPLES.SAMPLE_TARGET, [10, 10], 10, 0.998, False, False, False, False);
    template_clustering(FCPS_SAMPLES.SAMPLE_WING_NUT, [10, 10], 5, 0.998, False, False, False, False);
    template_clustering(FCPS_SAMPLES.SAMPLE_CHAINLINK, [10, 10], 15, 0.998, False, False, False, False);
    template_clustering(FCPS_SAMPLES.SAMPLE_TETRA, [7, 7], 5, 0.998, False, False, False, False);
    template_clustering(FCPS_SAMPLES.SAMPLE_HEPTA, [7, 7], 5, 0.998, False, False, False, False);


cluster_simple3();
cluster_simple4();
cluster_simple5();
cluster_lsun();
cluster_target();
cluster_two_diamonds();
cluster_chainlink();
cluster_hepta();
cluster_tetra();


# experiment_execution_time();