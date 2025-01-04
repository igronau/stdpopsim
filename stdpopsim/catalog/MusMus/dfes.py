import stdpopsim

_species = stdpopsim.get_species("MusMus")

###########################################################
#
# DFEs
#
###########################################################


def _BookerDFE():
    id = "Gamma_B21"
    description = "Deleterious Gamma DFE CDS"
    long_description = """
    Return negative MutationType()s representing a Mus
    musculus subsp. castaneous DFE for protein coded exons or CDS. Booker et al. (2021),
    https://doi.org/10.1101/2021.06.10.447924
    DFE parameters are based on an analysis of the unfolded site frequency spectrum
    (uSFS) using polyDFE v2 (Tataru and Bataillon 2019) as presented in Booker
    et al. (2021).
    """
    citations = [
        stdpopsim.Citation(
            author="Booker et al.",
            year=2021,
            doi="https://doi.org/10.1101/2021.06.10.447924",
            reasons={stdpopsim.CiteReason.DFE},  # include the dfe_model reason
        )
    ]
    neutral = stdpopsim.MutationType()
    gamma_shape = 0.186  # shape
    gamma_mean = -5.96e-02  # expected value
    h = 0.5  # dominance coefficient
    negative = stdpopsim.MutationType(
        dominance_coeff=h,
        distribution_type="g",  # gamma distribution
        distribution_args=[gamma_mean, gamma_shape],
    )

    return stdpopsim.DFE(
        id=id,
        description=description,
        long_description=long_description,
        mutation_types=[neutral, negative],
        proportions=[0.334, 0.666],
        citations=citations,
    )


_species.add_dfe(_BookerDFE())
