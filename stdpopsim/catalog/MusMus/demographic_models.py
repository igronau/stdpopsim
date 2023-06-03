import msprime
import numpy as np

import stdpopsim

_species = stdpopsim.get_species("MusMus")


def _dom_1pop():
    # the size during the interval times[k] to times[k+1] = sizes[k]
    times = np.array(
        [
            0,
            83,
            180,
            291,
            420,
            570,
            743,
            943,
            1175,
            1443,
            1754,
            2114,
            2530,
            3012,
            3570,
            4216,
            4964,
            5829,
            6831,
            7991,
            9334,
            10889,
            12688,
            14772,
            17183,
            19975,
            23207,
            26948,
            31279,
            36292,
            42096,
            48815,
            56592,
            65596,
            76019,
            88084,
            102052,
            118221,
            136938,
            158606,
            183689,
            212726,
            246340,
            285254,
            330300,
            382446,
            442812,
            512693,
            593589,
            687237,
            795646,
            921140,
            1066418,
            1234595,
            1429281,
            1654653,
            1915544,
        ]
    )
    sizes = np.array(
        [
            2040,
            2040,
            3844,
            90428,
            145603,
            111242,
            115399,
            147212,
            159142,
            136620,
            97250,
            58488,
            33028,
            18939,
            11758,
            8463,
            7480,
            8332,
            11240,
            16490,
            23419,
            29931,
            34163,
            36886,
            41195,
            50557,
            67337,
            90926,
            115426,
            131016,
            132063,
            121751,
            107067,
            93046,
            81892,
            74185,
            69939,
            69317,
            73097,
            82953,
            101471,
            131392,
            173264,
            222951,
            271935,
            309961,
            327217,
            316861,
            279833,
            227037,
            173594,
            131050,
            98811,
            98811,
            133912,
            133912,
            133912,
        ]
    )

    demographic_events = []
    for sz, t in zip(sizes, times):
        demographic_events.append(
            msprime.PopulationParametersChange(time=t, initial_size=sz, population_id=0)
        )

    populations = [
        stdpopsim.Population(
            id="M_musculus_domesticus",
            description="Mus musculus domesticus German population",
        )
    ]

    return stdpopsim.DemographicModel(
        id="DomesticusEurope_1F22",
        description="M. musculus domesticus piecewise constant size",
        long_description="""
            This model comes from MSMC using four randomly sampled
            individuals (DEU01,DEU03,DEU04,DEU06) from a German population.
            The model is estimated with 57 time periods.
        """,
        populations=populations,
        citations=[
            stdpopsim.Citation(
                author="Fujiwara et al.",
                year=2022,
                doi="https://doi.org/10.1093/gbe/evac068",
                reasons={stdpopsim.CiteReason.DEM_MODEL},
            )
        ],
        generation_time=1,
        mutation_rate=5.7e-9,
        demographic_events=demographic_events,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=sizes[0], metadata=populations[0].asdict()
            )
        ],
    )


_species.add_demographic_model(_dom_1pop())


def _mus_1pop():
    # the size during the interval times[k] to times[k+1] = sizes[k]
    times = np.array(
        [
            0,
            35,
            76,
            123,
            177,
            240,
            313,
            398,
            495,
            609,
            740,
            891,
            1067,
            1270,
            1505,
            1778,
            2093,
            2458,
            2881,
            3370,
            3936,
            4591,
            5350,
            6229,
            7246,
            8423,
            9785,
            11363,
            13189,
            15303,
            17750,
            20583,
            23863,
            27659,
            32054,
            37142,
            43031,
            49849,
            57741,
            66878,
            77455,
            89698,
            103872,
            120280,
            139274,
            161262,
            186716,
            216182,
            250293,
            289781,
            335491,
            388409,
            449667,
            520579,
            602670,
            697702,
            807711,
        ]
    )
    sizes = np.array(
        [
            179912,
            179912,
            8931,
            8035,
            9029,
            9960,
            12104,
            16254,
            25527,
            42715,
            61935,
            68111,
            55959,
            36220,
            20382,
            11222,
            6695,
            4605,
            3751,
            3643,
            4177,
            5506,
            7990,
            12072,
            17741,
            23546,
            26648,
            25399,
            21219,
            16747,
            13588,
            12259,
            13023,
            16339,
            22556,
            30806,
            38441,
            42857,
            43874,
            43467,
            43933,
            47001,
            54304,
            67725,
            88494,
            116547,
            151909,
            194969,
            245823,
            302950,
            359368,
            400867,
            407105,
            407105,
            152757,
            152757,
            152757,
        ]
    )

    demographic_events = []
    for sz, t in zip(sizes, times):
        demographic_events.append(
            msprime.PopulationParametersChange(time=t, initial_size=sz, population_id=0)
        )

    populations = [
        stdpopsim.Population(
            id="M_musculus_musculus",
            description="Mus musculus musculus Korean population",
        )
    ]

    return stdpopsim.DemographicModel(
        id="MusculusKorea_1F22",
        description="M. musculus musculus piecewise constant size",
        long_description="""
            This model comes from MSMC using four randomly sampled
            individuals (KOR01,KOR02,KOR03,KOR05) from a Korean population.
            The model is estimated with 57 time periods.
        """,
        populations=populations,
        citations=[
            stdpopsim.Citation(
                author="Fujiwara et al.",
                year=2022,
                doi="https://doi.org/10.1093/gbe/evac068",
                reasons={stdpopsim.CiteReason.DEM_MODEL},
            )
        ],
        generation_time=1,
        mutation_rate=5.7e-9,
        demographic_events=demographic_events,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=sizes[0], metadata=populations[0].asdict()
            )
        ],
    )


_species.add_demographic_model(_mus_1pop())
