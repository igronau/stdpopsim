"""
Genome, genetic map and demographic model definitions for humans.
"""
import math

import msprime

import stdpopsim.models as models
import stdpopsim.genomes as genomes
import stdpopsim.genetic_maps as genetic_maps


###########################################################
#
# Genetic maps
#
###########################################################


class HapmapII_GRCh37(genetic_maps.GeneticMap):
    """
    The Phase II HapMap Genetic map (lifted over to GRCh37) used in
    1000 Genomes. Please see the `README
    <ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/working/20110106_recombination_hotspots/README_hapmapII_GRCh37_map>`_
    for more details.
    """
    url = (
        "http://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/working/"
        "20110106_recombination_hotspots/"
        "HapmapII_GRCh37_RecombinationHotspots.tar.gz")
    file_pattern = "genetic_map_GRCh37_{name}.txt"


genetic_maps.register_genetic_map(HapmapII_GRCh37())

###########################################################
#
# Genome definition
#
###########################################################

# List of chromosomes. Data for length information based on DM6,
# https://www.ncbi.nlm.nih.gov/genome/?term=drosophila+melanogaster.
# FIXME: add mean mutation and recombination rate data to this table.
_chromosome_data = """\
chrX   23542271
chr2L   23513712
chr2R   25286936
chr3L   28110227
chr3R   32079331
chr4   1348131
chrY   3667352
chrM   19524
"""

_chromosomes = []
for line in _chromosome_data.splitlines():
    name, length = line.split()[:2]
    _chromosomes.append(genomes.Chromosome(
        name=name, length=int(length),
        mean_mutation_rate=8.4e-9,  # WRONG!, underestimate used in S&S
        mean_recombination_rate=1e-8))  # WRONG!


#: :class:`stdpopsim.Genome` definition for D. melanogaster. Chromosome length data is
# based on DM6
genome = genomes.Genome(
    species="drosophila_melanogaster",
    chromosomes=_chromosomes,
    default_genetic_map=None)


###########################################################
#
# Demographic models
#
###########################################################


class SheehanSongThreeEpoch(models.Model):
    """
    The three epoch model estimated for African samples from Sheehan and Song

    .. todo:: document this model, including the original publications
        and clear information about what the different population indexes
        mean.

    """

    def __init__(self):

        # Parameter values from "Simulating Data" section
        # these are assumptions, not estimates
        N_ref = 100000
        t_1_coal = 0.5
        t_2_coal = 5.0
        # estimates from the ANN
        N_R = 544200
        N_B = 145300
        N_A = 652700
        # Times are provided in 4N_ref generations, so we convert into generations.
        # generation_time = 10 / year
        t_1 = t_1_coal * 4 * N_ref
        t_2 = t_2_coal * 4 * N_ref
        # Population IDs correspond to their indexes in the population
        # configuration array. Therefore, we have 0=YRI, 1=CEU and 2=CHB
        # initially.
        self.population_configurations = [
            msprime.PopulationConfiguration(initial_size=N_R),
        ]
        self.demographic_events = [
            # Size change at bottleneck (back in time; BIT)
            msprime.PopulationParametersChange(
                time=t_1, initial_size=N_B, population_id=0),
            # Size change at recovery (BIT)
            msprime.PopulationParametersChange(
                time=t_2, initial_size=N_A, population_id=0)
        ]
