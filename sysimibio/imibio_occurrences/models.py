from django.db import models


class ImibioOccurrence(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gbifID = models.BigIntegerField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    accessRights = models.TextField(blank=True, null=True)
    accrualMethod = models.TextField(blank=True, null=True)
    accrualPeriodicity = models.TextField(blank=True, null=True)
    accrualPolicy = models.TextField(blank=True, null=True)
    alternative = models.TextField(blank=True, null=True)
    audience = models.TextField(blank=True, null=True)
    available = models.TextField(blank=True, null=True)
    bibliographicCitation = models.TextField(blank=True, null=True)
    conformsTo = models.TextField(blank=True, null=True)
    contributor = models.TextField(blank=True, null=True)
    coverage = models.TextField(blank=True, null=True)
    created = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    dateAccepted = models.TextField(blank=True, null=True)
    dateCopyrighted = models.TextField(blank=True, null=True)
    dateSubmitted = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    educationLevel = models.TextField(blank=True, null=True)
    extent = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    hasFormat = models.TextField(blank=True, null=True)
    hasPart = models.TextField(blank=True, null=True)
    hasVersion = models.TextField(blank=True, null=True)
    identifier = models.TextField(blank=True, null=True)
    instructionalMethod = models.TextField(blank=True, null=True)
    isFormatOf = models.TextField(blank=True, null=True)
    isPartOf = models.TextField(blank=True, null=True)
    isReferencedBy = models.TextField(blank=True, null=True)
    isReplacedBy = models.TextField(blank=True, null=True)
    isRequiredBy = models.TextField(blank=True, null=True)
    isVersionOf = models.TextField(blank=True, null=True)
    issued = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    license = models.TextField(blank=True, null=True)
    mediator = models.TextField(blank=True, null=True)
    medium = models.TextField(blank=True, null=True)
    modified = models.TextField(blank=True, null=True)
    provenance = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    relation = models.TextField(blank=True, null=True)
    replaces = models.TextField(blank=True, null=True)
    requires = models.TextField(blank=True, null=True)
    rights = models.TextField(blank=True, null=True)
    rightsHolder = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    spatial = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    tableOfContents = models.TextField(blank=True, null=True)
    temporal = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    valid = models.TextField(blank=True, null=True)
    institutionID = models.TextField(blank=True, null=True)
    collectionID = models.TextField(blank=True, null=True)
    datasetID = models.TextField(blank=True, null=True)
    institutionCode = models.TextField(blank=True, null=True)
    collectionCode = models.TextField(blank=True, null=True)
    datasetName = models.TextField(blank=True, null=True)
    ownerInstitutionCode = models.TextField(blank=True, null=True)
    basisOfRecord = models.TextField(blank=True, null=True)
    informationWithheld = models.TextField(blank=True, null=True)
    dataGeneralizations = models.TextField(blank=True, null=True)
    dynamicProperties = models.TextField(blank=True, null=True)
    occurrenceID = models.TextField(blank=True, null=True)
    catalogNumber = models.TextField(blank=True, null=True)
    recordNumber = models.TextField(blank=True, null=True)
    recordedBy = models.TextField(blank=True, null=True)
    individualCount = models.TextField(blank=True, null=True)
    organismQuantity = models.TextField(blank=True, null=True)
    organismQuantityType = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    lifeStage = models.TextField(blank=True, null=True)
    reproductiveCondition = models.TextField(blank=True, null=True)
    behavior = models.TextField(blank=True, null=True)
    establishmentMeans = models.TextField(blank=True, null=True)
    occurrenceStatus = models.TextField(blank=True, null=True)
    preparations = models.TextField(blank=True, null=True)
    disposition = models.TextField(blank=True, null=True)
    associatedReferences = models.TextField(blank=True, null=True)
    associatedSequences = models.TextField(blank=True, null=True)
    associatedTaxa = models.TextField(blank=True, null=True)
    otherCatalogNumbers = models.TextField(blank=True, null=True)
    occurrenceRemarks = models.TextField(blank=True, null=True)
    organismID = models.TextField(blank=True, null=True)
    organismName = models.TextField(blank=True, null=True)
    organismScope = models.TextField(blank=True, null=True)
    associatedOccurrences = models.TextField(blank=True, null=True)
    associatedOrganisms = models.TextField(blank=True, null=True)
    previousIdentifications = models.TextField(blank=True, null=True)
    organismRemarks = models.TextField(blank=True, null=True)
    materialSampleID = models.TextField(blank=True, null=True)
    eventID = models.TextField(blank=True, null=True)
    parentEventID = models.TextField(blank=True, null=True)
    fieldNumber = models.TextField(blank=True, null=True)
    eventDate = models.TextField(blank=True, null=True)
    eventTime = models.TextField(blank=True, null=True)
    startDayOfYear = models.BigIntegerField(blank=True, null=True)
    endDayOfYear = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    day = models.BigIntegerField(blank=True, null=True)
    verbatimEventDate = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    samplingProtocol = models.TextField(blank=True, null=True)
    samplingEffort = models.TextField(blank=True, null=True)
    sampleSizeValue = models.TextField(blank=True, null=True)
    sampleSizeUnit = models.TextField(blank=True, null=True)
    fieldNotes = models.TextField(blank=True, null=True)
    eventRemarks = models.TextField(blank=True, null=True)
    locationID = models.TextField(blank=True, null=True)
    higherGeographyID = models.TextField(blank=True, null=True)
    higherGeography = models.TextField(blank=True, null=True)
    continent = models.TextField(blank=True, null=True)
    waterBody = models.TextField(blank=True, null=True)
    islandGroup = models.TextField(blank=True, null=True)
    island = models.TextField(blank=True, null=True)
    countryCode = models.TextField(blank=True, null=True)
    stateProvince = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    municipality = models.TextField(blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    verbatimLocality = models.TextField(blank=True, null=True)
    verbatimElevation = models.TextField(blank=True, null=True)
    verbatimDepth = models.TextField(blank=True, null=True)
    minimumDistanceAboveSurfaceInMeters = models.TextField(blank=True, null=True)
    maximumDistanceAboveSurfaceInMeters = models.TextField(blank=True, null=True)
    locationAccordingTo = models.TextField(blank=True, null=True)
    locationRemarks = models.TextField(blank=True, null=True)
    decimalLatitude = models.FloatField(blank=True, null=True)
    decimalLongitude = models.FloatField(blank=True, null=True)
    coordinateUncertaintyInMeters = models.FloatField(blank=True, null=True)
    coordinatePrecision = models.TextField(blank=True, null=True)
    pointRadiusSpatialFit = models.TextField(blank=True, null=True)
    verbatimCoordinateSystem = models.TextField(blank=True, null=True)
    verbatimSRS = models.TextField(blank=True, null=True)
    footprintWKT = models.TextField(blank=True, null=True)
    footprintSRS = models.TextField(blank=True, null=True)
    footprintSpatialFit = models.TextField(blank=True, null=True)
    georeferencedBy = models.TextField(blank=True, null=True)
    georeferencedDate = models.TextField(blank=True, null=True)
    georeferenceProtocol = models.TextField(blank=True, null=True)
    georeferenceSources = models.TextField(blank=True, null=True)
    georeferenceVerificationStatus = models.TextField(blank=True, null=True)
    georeferenceRemarks = models.TextField(blank=True, null=True)
    geologicalContextID = models.TextField(blank=True, null=True)
    earliestEonOrLowestEonothem = models.TextField(blank=True, null=True)
    latestEonOrHighestEonothem = models.TextField(blank=True, null=True)
    earliestEraOrLowestErathem = models.TextField(blank=True, null=True)
    latestEraOrHighestErathem = models.TextField(blank=True, null=True)
    earliestPeriodOrLowestSystem = models.TextField(blank=True, null=True)
    latestPeriodOrHighestSystem = models.TextField(blank=True, null=True)
    earliestEpochOrLowestSeries = models.TextField(blank=True, null=True)
    latestEpochOrHighestSeries = models.TextField(blank=True, null=True)
    earliestAgeOrLowestStage = models.TextField(blank=True, null=True)
    latestAgeOrHighestStage = models.TextField(blank=True, null=True)
    lowestBiostratigraphicZone = models.TextField(blank=True, null=True)
    highestBiostratigraphicZone = models.TextField(blank=True, null=True)
    lithostratigraphicTerms = models.TextField(blank=True, null=True)
    group = models.TextField(blank=True, null=True)
    formation = models.TextField(blank=True, null=True)
    member = models.TextField(blank=True, null=True)
    bed = models.TextField(blank=True, null=True)
    identificationID = models.TextField(blank=True, null=True)
    identificationQualifier = models.TextField(blank=True, null=True)
    typeStatus = models.TextField(blank=True, null=True)
    identifiedBy = models.TextField(blank=True, null=True)
    dateIdentified = models.TextField(blank=True, null=True)
    identificationReferences = models.TextField(blank=True, null=True)
    identificationVerificationStatus = models.TextField(blank=True, null=True)
    identificationRemarks = models.TextField(blank=True, null=True)
    taxonID = models.TextField(blank=True, null=True)
    scientificNameID = models.TextField(blank=True, null=True)
    acceptedNameUsageID = models.TextField(blank=True, null=True)
    parentNameUsageID = models.TextField(blank=True, null=True)
    originalNameUsageID = models.TextField(blank=True, null=True)
    nameAccordingToID = models.TextField(blank=True, null=True)
    namePublishedInID = models.TextField(blank=True, null=True)
    taxonConceptID = models.TextField(blank=True, null=True)
    scientificName = models.TextField(blank=True, null=True)
    acceptedNameUsage = models.TextField(blank=True, null=True)
    parentNameUsage = models.TextField(blank=True, null=True)
    originalNameUsage = models.TextField(blank=True, null=True)
    nameAccordingTo = models.TextField(blank=True, null=True)
    namePublishedIn = models.TextField(blank=True, null=True)
    namePublishedInYear = models.TextField(blank=True, null=True)
    higherClassification = models.TextField(blank=True, null=True)
    kingdom = models.TextField(blank=True, null=True)
    phylum = models.TextField(blank=True, null=True)
    clase = models.CharField("class", max_length=254, blank=True, null=True)
    order = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    subgenus = models.TextField(blank=True, null=True)
    specificEpithet = models.TextField(blank=True, null=True)
    infraspecificEpithet = models.TextField(blank=True, null=True)
    taxonRank = models.TextField(blank=True, null=True)
    verbatimTaxonRank = models.TextField(blank=True, null=True)
    vernacularName = models.TextField(blank=True, null=True)
    nomenclaturalCode = models.TextField(blank=True, null=True)
    taxonomicStatus = models.TextField(blank=True, null=True)
    nomenclaturalStatus = models.TextField(blank=True, null=True)
    taxonRemarks = models.TextField(blank=True, null=True)
    datasetKey = models.TextField(blank=True, null=True)
    publishingCountry = models.TextField(blank=True, null=True)
    lastInterpreted = models.TextField(blank=True, null=True)
    elevation = models.TextField(blank=True, null=True)
    elevationAccuracy = models.TextField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    depthAccuracy = models.TextField(blank=True, null=True)
    distanceAboveSurface = models.TextField(blank=True, null=True)
    distanceAboveSurfaceAccuracy = models.TextField(blank=True, null=True)
    issue = models.TextField(blank=True, null=True)
    mediaType = models.TextField(blank=True, null=True)
    hasCoordinate = models.TextField(blank=True, null=True)
    hasGeospatialIssues = models.TextField(blank=True, null=True)
    taxonKey = models.BigIntegerField(blank=True, null=True)
    acceptedTaxonKey = models.BigIntegerField(blank=True, null=True)
    kingdomKey = models.BigIntegerField(blank=True, null=True)
    phylumKey = models.BigIntegerField(blank=True, null=True)
    classKey = models.BigIntegerField(blank=True, null=True)
    orderKey = models.BigIntegerField(blank=True, null=True)
    familyKey = models.BigIntegerField(blank=True, null=True)
    genusKey = models.BigIntegerField(blank=True, null=True)
    subgenusKey = models.TextField(blank=True, null=True)
    speciesKey = models.BigIntegerField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    genericName = models.TextField(blank=True, null=True)
    acceptedScientificName = models.TextField(blank=True, null=True)
    verbatimScientificName = models.TextField(blank=True, null=True)
    typifiedName = models.TextField(blank=True, null=True)
    protocol = models.TextField(blank=True, null=True)
    lastParsed = models.TextField(blank=True, null=True)
    lastCrawled = models.TextField(blank=True, null=True)
    repatriated = models.TextField(blank=True, null=True)
    relativeOrganismQuantity = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
