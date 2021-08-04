
from django_neomodel import DjangoNode
from neomodel import (config, StructuredNode, Property, StringProperty, IntegerProperty,
                      UniqueIdProperty, BooleanProperty, DateProperty, DateTimeProperty,
                      ArrayProperty, JSONProperty, FloatProperty, RelationshipTo, RelationshipFrom)
from createobject.set_relationship import create_relationship_to,create_relationship_from,create_relationship

config.DATABASE_URL = 'bolt://neo4j:123123@localhost:7687'


class Meta:
    app_label = 'createobject'


class Thing(DjangoNode):
    additionalType = create_relationship_to(['Text'], '附加类型')

    alternateName = create_relationship_to(['Text'], '别名')

    description = create_relationship_to(['Text'], '描述')

    disambiguatingDescription = create_relationship_to(['Text'], '消歧描述')

    identifier = create_relationship_to(['LocationFeatureSpecification', 'PropertyValue', 'Text'], '标识符')

    image = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '图片')

    mainEntityOfPage = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork', 'Text'], '页面的核心实体')

    name = StringProperty()

    monitor_id = IntegerProperty()

    potentialAction = create_relationship_to(['AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'Action'], '预期的行动')

    sameAs = create_relationship_to(['Text'], '等同')

    url = create_relationship_to(['Text'], '链接')


class Action(Thing):
    actionStatus = create_relationship_to(['ActionStatusType'], '执行操作的状态')

    agent = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '行为的发起者')

    endTime = create_relationship_to(['Date'], '结束时刻')

    error = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '错误')

    instrument = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '工具')

    location = create_relationship_to(['PostalAddress', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text'], '地点')

    object = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '行动操作的对象')

    participant = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '参与者')

    result = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '行动的结果')

    startTime = create_relationship_to(['Date'], '开始时刻')

    target = create_relationship_to(['EntryPoint'], '目标')


class MoveAction(Action):
    fromLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '发源地')

    toLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '到什么地方')


class TravelAction(MoveAction):
    distance = create_relationship_to(['Distance'], '距离')


class DepartAction(MoveAction):
    pass


class ArriveAction(MoveAction):
    pass


class TransferAction(Action):
    fromLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '发源地')

    toLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '到什么地方')


class DownloadAction(TransferAction):
    pass


class LendAction(TransferAction):
    borrower = create_relationship_to(['Person'], '借入者')


class GiveAction(TransferAction):
    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class ReceiveAction(TransferAction):
    deliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '物流送货方式')

    sender = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience', 'Person'], '发送者')


class SendAction(TransferAction):
    deliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '物流送货方式')

    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class BorrowAction(TransferAction):
    lender = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '借出者')


class ReturnAction(TransferAction):
    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class TakeAction(TransferAction):
    pass


class TradeAction(Action):
    price = create_relationship_to(['Integer', 'Text'], '价格')

    priceSpecification = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '价格明细')


class QuoteAction(TradeAction):
    pass


class SellAction(TradeAction):
    buyer = create_relationship_to(['Person'], '买家')


class PayAction(TradeAction):
    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class RentAction(TradeAction):
    landlord = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '房东')

    realEstateAgent = create_relationship_to(['RealEstateAgent'], '房地产中介')


class DonateAction(TradeAction):
    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class OrderAction(TradeAction):
    deliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '物流送货方式')


class BuyAction(TradeAction):
    seller = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '卖家')


class TipAction(TradeAction):
    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class ControlAction(Action):
    pass


class ResumeAction(ControlAction):
    pass


class DeactivateAction(ControlAction):
    pass


class ActivateAction(ControlAction):
    pass


class SuspendAction(ControlAction):
    pass


class AchieveAction(Action):
    pass


class LoseAction(AchieveAction):
    winner = create_relationship_to(['Person'], '赢家')


class WinAction(AchieveAction):
    loser = create_relationship_to(['Person'], '输家')


class TieAction(AchieveAction):
    pass


class OrganizeAction(Action):
    pass


class ApplyAction(OrganizeAction):
    pass


class PlanAction(OrganizeAction):
    scheduledTime = create_relationship_to(['Date'], '预约的时间')


class CancelAction(PlanAction):
    pass


class ReserveAction(PlanAction):
    pass


class ScheduleAction(PlanAction):
    pass


class AllocateAction(OrganizeAction):
    pass


class AuthorizeAction(AllocateAction):
    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class AssignAction(AllocateAction):
    pass


class RejectAction(AllocateAction):
    pass


class AcceptAction(AllocateAction):
    pass


class BookmarkAction(OrganizeAction):
    pass


class AssessAction(Action):
    pass


class IgnoreAction(AssessAction):
    pass


class ChooseAction(AssessAction):
    actionOption = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing', 'Text'], '执行操作的选项')


class VoteAction(ChooseAction):
    candidate = create_relationship_to(['Person'], '候选人')


class ReactAction(AssessAction):
    pass


class LikeAction(ReactAction):
    pass


class DisagreeAction(ReactAction):
    pass


class EndorseAction(ReactAction):
    endorsee = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '背书支持')


class AgreeAction(ReactAction):
    pass


class DislikeAction(ReactAction):
    pass


class WantAction(ReactAction):
    pass


class ReviewAction(AssessAction):
    resultReview = create_relationship_to(['ClaimReview', 'Review'], '行动的评论')


class InteractAction(Action):
    pass


class BefriendAction(InteractAction):
    pass


class RegisterAction(InteractAction):
    pass


class SubscribeAction(InteractAction):
    pass


class LeaveAction(InteractAction):
    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')


class UnRegisterAction(InteractAction):
    pass


class MarryAction(InteractAction):
    pass


class JoinAction(InteractAction):
    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')


class CommunicateAction(InteractAction):
    about = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '关于')

    inLanguage = create_relationship_to(['Text', 'Language'], '使用语言')

    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')


class CheckOutAction(CommunicateAction):
    pass


class InviteAction(CommunicateAction):
    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')


class CommentAction(CommunicateAction):
    resultComment = create_relationship_to(['Answer', 'Comment'], '行动的结论')


class ReplyAction(CommunicateAction):
    resultComment = create_relationship_to(['Answer', 'Comment'], '行动的结论')


class ShareAction(CommunicateAction):
    pass


class InformAction(CommunicateAction):
    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')


class RsvpAction(InformAction):
    additionalNumberOfGuests = create_relationship_to(['Integer'], '其余的客户人数')

    comment = create_relationship_to(['Answer', 'Comment'], '评论')

    rsvpResponse = create_relationship_to(['RsvpResponseType'], '对请柬的回复')


class ConfirmAction(InformAction):
    pass


class AskAction(CommunicateAction):
    question = create_relationship_to(['Question'], '问题')


class CheckInAction(CommunicateAction):
    pass


class FollowAction(InteractAction):
    followee = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '被关注')


class ConsumeAction(Action):
    expectsAcceptanceOf = create_relationship_to(['AggregateOffer', 'Offer'], '行动前必须接受的条件')


class ViewAction(ConsumeAction):
    pass


class DrinkAction(ConsumeAction):
    pass


class ListenAction(ConsumeAction):
    pass


class WatchAction(ConsumeAction):
    pass


class UseAction(ConsumeAction):
    pass


class WearAction(UseAction):
    pass


class InstallAction(ConsumeAction):
    pass


class ReadAction(ConsumeAction):
    pass


class EatAction(ConsumeAction):
    pass


class CreateAction(Action):
    pass


class DrawAction(CreateAction):
    pass


class FilmAction(CreateAction):
    pass


class CookAction(CreateAction):
    foodEstablishment = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '餐饮场所')

    foodEvent = create_relationship_to(['FoodEvent'], '食物事件发生的地点')

    recipe = create_relationship_to(['Recipe'], '菜谱')


class PhotographAction(CreateAction):
    pass


class PaintAction(CreateAction):
    pass


class WriteAction(CreateAction):
    inLanguage = create_relationship_to(['Text', 'Language'], '使用语言')


class PlayAction(Action):
    audience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '受众')

    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')


class ExerciseAction(PlayAction):
    distance = create_relationship_to(['Distance'], '距离')

    exerciseCourse = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '锻炼场地')

    fromLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '发源地')

    opponent = create_relationship_to(['Person'], '对手')

    sportsActivityLocation = create_relationship_to(['SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'SportsActivityLocation'], '运动场所')

    sportsEvent = create_relationship_to(['SportsEvent'], '运动有关的活动')

    sportsTeam = create_relationship_to(['SportsTeam'], '参赛队伍')

    toLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '到什么地方')


class PerformAction(PlayAction):
    entertainmentBusiness = create_relationship_to(['MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'EntertainmentBusiness'], '娱乐业')


class SearchAction(Action):
    query = create_relationship_to(['Text'], '查询')


class FindAction(Action):
    pass


class TrackAction(FindAction):
    deliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '物流送货方式')


class CheckAction(FindAction):
    pass


class DiscoverAction(FindAction):
    pass


class UpdateAction(Action):
    targetCollection = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '行动要达到的目标')


class AddAction(UpdateAction):
    pass


class InsertAction(AddAction):
    toLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '到什么地方')


class AppendAction(InsertAction):
    pass


class PrependAction(InsertAction):
    pass


class DeleteAction(UpdateAction):
    pass


class ReplaceAction(UpdateAction):
    replacee = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '被替代者')

    replacer = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '替代者')


class CreativeWork(Thing):
    about = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '关于')

    accessMode = create_relationship_to(['Text'], '感知形式')

    accessModeSufficient = create_relationship_to(['Text'], '全部感知形式')

    accessibilityAPI = create_relationship_to(['Text'], '无障碍环境服务API')

    accessibilityControl = create_relationship_to(['Text'], '无障碍环境服务控制方法')

    accessibilityFeature = create_relationship_to(['Text'], '无障碍环境服务内容特性')

    accessibilityHazard = create_relationship_to(['Text'], '无障碍环境服务的连带风险')

    accessibilitySummary = create_relationship_to(['Text'], '无障碍环境服务的总结')

    accountablePerson = create_relationship_to(['Person'], '负责人')

    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    alternativeHeadline = create_relationship_to(['Text'], '副标题')

    associatedMedia = create_relationship_to(['MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'MediaObject'], '相关媒体对象')

    audience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '受众')

    audio = create_relationship_to(['AudioObject'], '音频')

    author = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '作者')

    award = create_relationship_to(['Text'], '所获奖项')

    character = create_relationship_to(['Person'], '人物角色')

    citation = create_relationship_to(['Text', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '引用')

    comment = create_relationship_to(['Answer', 'Comment'], '评论')

    commentCount = create_relationship_to(['Integer'], '评论总数')

    contentLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '所描述的地点')

    contentRating = create_relationship_to(['AggregateRating', 'Rating', 'Text'], '内容的评级')

    contributor = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '贡献者')

    copyrightHolder = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '版权所有者')

    copyrightYear = create_relationship_to(['Integer'], '版权年份')

    creator = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '作者')

    dateCreated = create_relationship_to(['Date'], '创建日期')

    dateModified = create_relationship_to(['Date'], '更新日期')

    datePublished = create_relationship_to(['Date'], '首发日期')

    discussionUrl = create_relationship_to(['Text'], '讨论URL')

    editor = create_relationship_to(['Person'], '编辑者')

    educationalAlignment = create_relationship_to(['AlignmentObject'], '对应的教学达标要求')

    educationalUse = create_relationship_to(['Text'], '教育用途')

    encoding = create_relationship_to(['MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'MediaObject'], '编码')

    encodingFormat = create_relationship_to(['Text'], '编码格式')

    exampleOfWork = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '范例作品')

    expires = create_relationship_to(['Date'], '过期日期')

    funder = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '投资者')

    genre = create_relationship_to(['Text'], '风格')

    hasPart = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '作品组件')

    headline = create_relationship_to(['Text'], '文章标题')

    inLanguage = create_relationship_to(['Text', 'Language'], '使用语言')

    interactionStatistic = create_relationship_to(['InteractionCounter'], '交互统计')

    interactivityType = create_relationship_to(['Text'], '交互类型')

    isAccessibleForFree = create_relationship_to(['Bool'], '是否免费')

    isBasedOn = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'Text'], '上游资源URL')

    isFamilyFriendly = create_relationship_to(['Bool'], '是否适合全家观看')

    isPartOf = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '从属于')

    keywords = create_relationship_to(['Text'], '关键词')

    learningResourceType = create_relationship_to(['Text'], '学习资料类型')

    license = create_relationship_to(['Text', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '许可证书')

    locationCreated = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '创建地点')

    mainEntity = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '核心实体')

    material = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'Text'], '材质')

    mentions = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '提到的实体')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')

    position = create_relationship_to(['Text', 'Integer'], '位置')

    producer = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作人')

    provider = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '提供方')

    publication = create_relationship_to(['BroadcastEvent', 'OnDemandEvent', 'PublicationEvent'], '发布活动')

    publisher = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '出版商')

    publishingPrinciples = create_relationship_to(['Text', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '出版准则')

    recordedAt = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '对应的活动')

    releasedEvent = create_relationship_to(['BroadcastEvent', 'OnDemandEvent', 'PublicationEvent'], '发布活动')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    schemaVersion = create_relationship_to(['Text'], 'schema的版本号')

    sourceOrganization = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '作者所属机构')

    spatialCoverage = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '数据集对应的地区')

    sponsor = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '赞助者')

    temporalCoverage = create_relationship_to(['Text', 'Date'], '数据集的时间跨度')

    text = create_relationship_to(['Text'], '文本')

    thumbnailUrl = create_relationship_to(['Text'], '缩略图链接')

    timeRequired = create_relationship_to(['Duration'], '所需时间')

    translator = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '翻译者')

    typicalAgeRange = create_relationship_to(['Text'], '适应年龄段')

    version = create_relationship_to(['Text', 'Integer'], '版本')

    video = create_relationship_to(['VideoObject'], '视频')

    workExample = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '作品的范例')


class Photograph(CreativeWork):
    pass


class Dataset(CreativeWork):
    distribution = create_relationship_to(['DataDownload'], '数据集的下载版本')

    includedInDataCatalog = create_relationship_to(['DataCatalog'], '所在数据集目录')

    issn = create_relationship_to(['Text'], 'ISSN号')


class DataFeed(Dataset):
    dataFeedElement = create_relationship_to(['Text', 'DataFeedItem', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '数据源的一条记录')


class Painting(CreativeWork):
    pass


class Course(CreativeWork):
    courseCode = create_relationship_to(['Text'], '课程的代码')

    coursePrerequisites = create_relationship_to(['Text', 'AlignmentObject', 'Course'], '课程必需的预备知识')

    hasCourseInstance = create_relationship_to(['CourseInstance'], '课程实例')


class HowTo(CreativeWork):
    estimatedCost = create_relationship_to(['MonetaryAmount', 'Text'], '相关物料的估价')

    performTime = create_relationship_to(['Duration'], '执行时间')

    prepTime = create_relationship_to(['Duration'], '准备时间')

    step = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork', 'Text'], '相关操作步骤')

    supply = create_relationship_to(['Text', 'HowToSupply'], '相关物料')

    tool = create_relationship_to(['HowToTool', 'Text'], '相关工具')

    totalTime = create_relationship_to(['Duration'], '总时间')

    yielded = create_relationship_to(['QuantitativeValue', 'Text'], '相关产出')


class Recipe(HowTo):
    cookTime = create_relationship_to(['Duration'], '烹饪时间')

    cookingMethod = create_relationship_to(['Text'], '烹饪方法')

    nutrition = create_relationship_to(['NutritionInformation'], '营养成分')

    recipeCategory = create_relationship_to(['Text'], '菜谱分类')

    recipeCuisine = create_relationship_to(['Text'], '菜谱的菜系')

    recipeIngredient = create_relationship_to(['Text'], '菜谱的食材')

    recipeInstructions = create_relationship_to(['OfferCatalog', 'BreadcrumbList', 'HowToSection', 'HowToStep', 'ItemList', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToTip', 'CreativeWork', 'Text'], '菜谱的做法')

    recipeYield = create_relationship_to(['QuantitativeValue', 'Text'], '菜谱的产出')

    suitableForDiet = create_relationship_to(['RestrictedDiet'], '适用的饮食')


class VisualArtwork(CreativeWork):
    artEdition = create_relationship_to(['Text', 'Integer'], '拷贝（副本）数量')

    artMedium = create_relationship_to(['Text'], '艺术材料')

    artform = create_relationship_to(['Text'], '艺术形式')

    artworkSurface = create_relationship_to(['Text'], '艺术作品材质')

    depth = create_relationship_to(['QuantitativeValue', 'Distance'], '深度')

    height = create_relationship_to(['Distance', 'QuantitativeValue'], '高度')

    width = create_relationship_to(['Distance', 'QuantitativeValue'], '宽度')


class Game(CreativeWork):
    characterAttribute = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '人物角色属性')

    gameItem = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '游戏道具')

    gameLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text', 'PostalAddress'], '游戏地址')

    numberOfPlayers = create_relationship_to(['QuantitativeValue'], '玩家数')

    quest = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '游戏任务')


class Season(CreativeWork):
    pass


class PublicationVolume(CreativeWork):
    pageEnd = create_relationship_to(['Integer', 'Text'], '结束页码')

    pageStart = create_relationship_to(['Text', 'Integer'], '开始页码')

    pagination = create_relationship_to(['Text'], '起止页码')

    volumeNumber = create_relationship_to(['Text', 'Integer'], '期刊的卷号')


class MusicRecording(CreativeWork):
    byArtist = create_relationship_to(['MusicGroup'], '艺人')

    duration = create_relationship_to(['Duration'], '持续时间')

    inAlbum = create_relationship_to(['MusicAlbum'], '所属专辑')

    inPlaylist = create_relationship_to(['MusicRelease', 'MusicAlbum', 'MusicPlaylist'], '所属播放列表')

    isrcCode = create_relationship_to(['Text'], '国际标准音像制品代码')

    recordingOf = create_relationship_to(['MusicComposition'], '对应的音乐作品')


class PublicationIssue(CreativeWork):
    issueNumber = create_relationship_to(['Text', 'Integer'], '期刊号')

    pageEnd = create_relationship_to(['Integer', 'Text'], '结束页码')

    pageStart = create_relationship_to(['Text', 'Integer'], '开始页码')

    pagination = create_relationship_to(['Text'], '起止页码')


class Article(CreativeWork):
    articleBody = create_relationship_to(['Text'], '文章正文')

    articleSection = create_relationship_to(['Text'], '文章所在栏目')

    pageEnd = create_relationship_to(['Integer', 'Text'], '结束页码')

    pageStart = create_relationship_to(['Text', 'Integer'], '开始页码')

    pagination = create_relationship_to(['Text'], '起止页码')

    wordCount = create_relationship_to(['Integer'], '字数')


class Report(Article):
    reportNumber = create_relationship_to(['Text'], '报告编号')


class TechArticle(Article):
    dependencies = create_relationship_to(['Text'], '依赖的先决条件')

    proficiencyLevel = create_relationship_to(['Text'], '熟练度水平')


class APIReference(TechArticle):
    assemblyVersion = create_relationship_to(['Text'], '程序库版本')

    executableLibraryName = create_relationship_to(['Text'], '可执行链接库名称')

    programmingModel = create_relationship_to(['Text'], '是否托管代码')

    targetPlatform = create_relationship_to(['Text'], '软件应用的目标硬件平台')


class SocialMediaPosting(Article):
    sharedContent = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '分享的内容')


class DiscussionForumPosting(SocialMediaPosting):
    pass


class BlogPosting(SocialMediaPosting):
    pass


class LiveBlogPosting(BlogPosting):
    coverageEndTime = create_relationship_to(['Date'], '博客直播结束时间')

    coverageStartTime = create_relationship_to(['Date'], '博客直播开始时间')

    liveBlogUpdate = create_relationship_to(['LiveBlogPosting', 'BlogPosting'], '博客直播的一条更新')


class ScholarlyArticle(Article):
    pass


class NewsArticle(Article):
    dateline = create_relationship_to(['Text'], '发稿地点')

    printColumn = create_relationship_to(['Text'], '印刷品所在列数')

    printEdition = create_relationship_to(['Text'], '印刷品版本')

    printPage = create_relationship_to(['Text'], '印刷品所在页面')

    printSection = create_relationship_to(['Text'], '印刷品所在栏目')


class WebPageElement(CreativeWork):
    pass


class WPFooter(WebPageElement):
    pass


class SiteNavigationElement(WebPageElement):
    pass


class WPAdBlock(WebPageElement):
    pass


class WPSideBar(WebPageElement):
    pass


class WPHeader(WebPageElement):
    pass


class Table(WebPageElement):
    pass


class MenuSection(CreativeWork):
    hasMenuItem = create_relationship_to(['MenuItem'], '菜单')

    hasMenuSection = create_relationship_to(['MenuSection'], '菜单子目录')


class WebSite(CreativeWork):
    issn = create_relationship_to(['Text'], 'ISSN号')


class Movie(CreativeWork):
    actor = create_relationship_to(['Person'], '演员')

    countryOfOrigin = create_relationship_to(['Country'], '影片制作国家')

    director = create_relationship_to(['Person'], '导演')

    duration = create_relationship_to(['Duration'], '持续时间')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    subtitleLanguage = create_relationship_to(['Text', 'Language'], '字幕语言')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class SoftwareApplication(CreativeWork):
    applicationCategory = create_relationship_to(['Text'], '软件应用的分类')

    applicationSubCategory = create_relationship_to(['Text'], '软件应用的子分类')

    applicationSuite = create_relationship_to(['Text'], '软件应用套装')

    availableOnDevice = create_relationship_to(['Text'], '支持的设备')

    countriesNotSupported = create_relationship_to(['Text'], '不支持的国家')

    countriesSupported = create_relationship_to(['Text'], '支持的国家')

    downloadUrl = create_relationship_to(['Text'], '下载链接')

    featureList = create_relationship_to(['Text'], '功能列表')

    fileSize = create_relationship_to(['Text'], '文件大小')

    installUrl = create_relationship_to(['Text'], 'APP安装地址')

    memoryRequirements = create_relationship_to(['Text'], '最低内存要求')

    operatingSystem = create_relationship_to(['Text'], '操作系统')

    permissions = create_relationship_to(['Text'], '权限')

    processorRequirements = create_relationship_to(['Text'], '处理器要求')

    releaseNotes = create_relationship_to(['Text'], '发布说明')

    screenshot = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '截图')

    softwareAddOn = create_relationship_to(['VideoGame', 'WebApplication', 'MobileApplication', 'SoftwareApplication'], '软件的插件')

    softwareHelp = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '软件的帮助文档')

    softwareRequirements = create_relationship_to(['Text'], '软件的运行要求')

    softwareVersion = create_relationship_to(['Text'], '软件的版本')

    storageRequirements = create_relationship_to(['Text'], '所需磁盘空间')

    supportingData = create_relationship_to(['DataFeed'], '软件应用所需的数据')


class MobileApplication(SoftwareApplication):
    carrierRequirements = create_relationship_to(['Text'], '运营商要求')


class WebApplication(SoftwareApplication):
    browserRequirements = create_relationship_to(['Text'], '浏览器要求')


class Code(CreativeWork):
    pass


class Sculpture(CreativeWork):
    pass


class Map(CreativeWork):
    mapType = create_relationship_to(['MapCategoryType'], '地图类型')


class Comment(CreativeWork):
    downvoteCount = create_relationship_to(['Integer'], '反对总数')

    parentItem = create_relationship_to(['Question'], '上级条目')

    upvoteCount = create_relationship_to(['Integer'], '支持总数')


class Answer(Comment):
    pass


class MusicComposition(CreativeWork):
    composer = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '作曲者')

    firstPerformance = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '首演')

    includedComposition = create_relationship_to(['MusicComposition'], '包含乐曲')

    iswcCode = create_relationship_to(['Text'], '国际标准音乐作品编码')

    lyricist = create_relationship_to(['Person'], '作词者')

    lyrics = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '歌词')

    musicArrangement = create_relationship_to(['MusicComposition'], '改编曲')

    musicCompositionForm = create_relationship_to(['Text'], '乐曲形式')

    musicalKey = create_relationship_to(['Text'], '音乐的调')

    recordedAs = create_relationship_to(['MusicRecording'], '录音')


class WebPage(CreativeWork):
    breadcrumb = create_relationship_to(['BreadcrumbList', 'Text'], '面包屑')

    lastReviewed = create_relationship_to(['Date'], '最近审查时间')

    mainContentOfPage = create_relationship_to(['WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebPageElement'], '是否网页主题')

    primaryImageOfPage = create_relationship_to(['Barcode', 'ImageObject'], '页面里的主要图片')

    relatedLink = create_relationship_to(['Text'], '相关链接')

    reviewedBy = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '评论者')

    significantLink = create_relationship_to(['Text'], '主要对外链接')

    specialty = create_relationship_to(['Specialty'], '特长')


class AboutPage(WebPage):
    pass


class QAPage(WebPage):
    pass


class CheckoutPage(WebPage):
    pass


class ProfilePage(WebPage):
    pass


class SearchResultsPage(WebPage):
    pass


class ContactPage(WebPage):
    pass


class CollectionPage(WebPage):
    pass


class VideoGallery(CollectionPage):
    pass


class ImageGallery(CollectionPage):
    pass


class ItemPage(WebPage):
    pass


class Conversation(CreativeWork):
    pass


class Message(CreativeWork):
    bccRecipient = create_relationship_to(['PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '密送')

    ccRecipient = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'PostalAddress', 'ContactPoint'], '抄送')

    dateRead = create_relationship_to(['Date'], '阅读日期')

    dateReceived = create_relationship_to(['Date'], '接收日期')

    dateSent = create_relationship_to(['Date'], '发送日期')

    messageAttachment = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '消息附件')

    recipient = create_relationship_to(['Person', 'PostalAddress', 'ContactPoint', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '接收者')

    sender = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience', 'Person'], '发送者')

    toRecipient = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person', 'PostalAddress', 'ContactPoint', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '收件人')


class EmailMessage(Message):
    pass


class Book(CreativeWork):
    bookEdition = create_relationship_to(['Text'], '书籍版本')

    bookFormat = create_relationship_to(['BookFormatType'], '书籍格式')

    illustrator = create_relationship_to(['Person'], '插图绘制者')

    isbn = create_relationship_to(['Text'], 'ISBN码')

    numberOfPages = create_relationship_to(['Integer'], '总页数')


class Menu(CreativeWork):
    hasMenuItem = create_relationship_to(['MenuItem'], '菜单')

    hasMenuSection = create_relationship_to(['MenuSection'], '菜单子目录')


class Question(CreativeWork):
    acceptedAnswer = create_relationship_to(['OfferCatalog', 'BreadcrumbList', 'HowToSection', 'HowToStep', 'ItemList', 'Answer'], '被采纳的答案')

    answerCount = create_relationship_to(['Integer'], '回答的总数')

    downvoteCount = create_relationship_to(['Integer'], '反对总数')

    suggestedAnswer = create_relationship_to(['OfferCatalog', 'BreadcrumbList', 'HowToSection', 'HowToStep', 'ItemList', 'Answer'], '建议的答案')

    upvoteCount = create_relationship_to(['Integer'], '支持总数')


class Blog(CreativeWork):
    blogPost = create_relationship_to(['LiveBlogPosting', 'BlogPosting'], '博客文章')

    issn = create_relationship_to(['Text'], 'ISSN号')


class Episode(CreativeWork):
    actor = create_relationship_to(['Person'], '演员')

    director = create_relationship_to(['Person'], '导演')

    episodeNumber = create_relationship_to(['Text', 'Integer'], '剧集编号')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    partOfSeason = create_relationship_to(['RadioSeason', 'TVSeason', 'CreativeWorkSeason'], '所属季')

    partOfSeries = create_relationship_to(['MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'CreativeWorkSeries'], '所属系列')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class TVEpisode(Episode):
    countryOfOrigin = create_relationship_to(['Country'], '影片制作国家')

    subtitleLanguage = create_relationship_to(['Text', 'Language'], '字幕语言')


class RadioEpisode(Episode):
    pass


class Review(CreativeWork):
    itemReviewed = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '评价物品')

    reviewBody = create_relationship_to(['Text'], '评论的正文')

    reviewRating = create_relationship_to(['AggregateRating', 'Rating'], '评论的打分')


class ClaimReview(Review):
    claimReviewed = create_relationship_to(['Text'], '被评价的声明')


class SoftwareSourceCode(CreativeWork):
    codeRepository = create_relationship_to(['Text'], '代码库')

    codeSampleType = create_relationship_to(['Text'], '代码示例的类型')

    programmingLanguage = create_relationship_to(['ComputerLanguage', 'Text'], '编程语言')

    runtimePlatform = create_relationship_to(['Text'], '运行平台')

    targetProduct = create_relationship_to(['VideoGame', 'WebApplication', 'MobileApplication', 'SoftwareApplication'], '软件应用的目标操作系统')


class Clip(CreativeWork):
    actor = create_relationship_to(['Person'], '演员')

    clipNumber = create_relationship_to(['Integer', 'Text'], '片段编号')

    director = create_relationship_to(['Person'], '导演')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    partOfEpisode = create_relationship_to(['RadioEpisode', 'TVEpisode', 'Episode'], '所属剧集')

    partOfSeason = create_relationship_to(['RadioSeason', 'TVSeason', 'CreativeWorkSeason'], '所属季')

    partOfSeries = create_relationship_to(['MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'CreativeWorkSeries'], '所属系列')


class VideoGameClip(Clip):
    pass


class RadioClip(Clip):
    pass


class TVClip(Clip):
    pass


class MovieClip(Clip):
    pass


class DigitalDocument(CreativeWork):
    hasDigitalDocumentPermission = create_relationship_to(['DigitalDocumentPermission'], '数字文档访问权限')


class TextDigitalDocument(DigitalDocument):
    pass


class PresentationDigitalDocument(DigitalDocument):
    pass


class SpreadsheetDigitalDocument(DigitalDocument):
    pass


class NoteDigitalDocument(DigitalDocument):
    pass


class DataCatalog(CreativeWork):
    dataset = create_relationship_to(['DataFeed', 'Dataset'], '数据集')


class MusicPlaylist(CreativeWork):
    numTracks = create_relationship_to(['Integer'], '音轨数')

    track = create_relationship_to(['MusicRecording', 'OfferCatalog', 'BreadcrumbList', 'HowToSection', 'HowToStep', 'ItemList'], '音轨')


class MusicAlbum(MusicPlaylist):
    albumProductionType = create_relationship_to(['MusicAlbumProductionType'], '专辑制作类型')

    albumRelease = create_relationship_to(['MusicRelease'], '专辑发行版本')

    albumReleaseType = create_relationship_to(['MusicAlbumReleaseType'], '专辑发行类型')

    byArtist = create_relationship_to(['MusicGroup'], '艺人')


class MusicRelease(MusicPlaylist):
    catalogNumber = create_relationship_to(['Text'], '目录中的编号')

    creditedTo = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '贡献者')

    duration = create_relationship_to(['Duration'], '持续时间')

    musicReleaseFormat = create_relationship_to(['MusicReleaseFormatType'], '音乐发行格式')

    recordLabel = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '唱片公司')

    releaseOf = create_relationship_to(['MusicAlbum'], '对应的专辑')


class MediaObject(CreativeWork):
    associatedArticle = create_relationship_to(['NewsArticle'], '相关文章')

    bitrate = create_relationship_to(['Text'], '比特率')

    contentSize = create_relationship_to(['Text'], '内容的文件大小')

    contentUrl = create_relationship_to(['Text'], '内容的访问链接')

    duration = create_relationship_to(['Duration'], '持续时间')

    embedUrl = create_relationship_to(['Text'], '嵌入URL')

    encodesCreativeWork = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '对应的作品')

    encodingFormat = create_relationship_to(['Text'], '编码格式')

    height = create_relationship_to(['Distance', 'QuantitativeValue'], '高度')

    playerType = create_relationship_to(['Text'], '播放器类型')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    regionsAllowed = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '允许播放的地区')

    requiresSubscription = create_relationship_to(['Bool'], '是否需要订阅')

    uploadDate = create_relationship_to(['Date'], '上传日期')

    width = create_relationship_to(['Distance', 'QuantitativeValue'], '宽度')


class AudioObject(MediaObject):
    transcript = create_relationship_to(['Text'], '文字记录')


class ImageObject(MediaObject):
    caption = create_relationship_to(['Text'], '标题')

    exifData = create_relationship_to(['Text', 'LocationFeatureSpecification', 'PropertyValue'], '图片对象的EXIF信息')

    representativeOfPage = create_relationship_to(['Bool'], '作为主题图所对应的页面')

    thumbnail = create_relationship_to(['Barcode', 'ImageObject'], '缩略图')


class Barcode(ImageObject):
    pass


class MusicVideoObject(MediaObject):
    pass


class VideoObject(MediaObject):
    actor = create_relationship_to(['Person'], '演员')

    caption = create_relationship_to(['Text'], '标题')

    director = create_relationship_to(['Person'], '导演')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    thumbnail = create_relationship_to(['Barcode', 'ImageObject'], '缩略图')

    transcript = create_relationship_to(['Text'], '文字记录')

    videoFrameSize = create_relationship_to(['Text'], '视频画面尺寸')

    videoQuality = create_relationship_to(['Text'], '视频画质')


class DataDownload(MediaObject):
    pass


class CreativeWorkSeason(CreativeWork):
    actor = create_relationship_to(['Person'], '演员')

    director = create_relationship_to(['Person'], '导演')

    endDate = create_relationship_to(['Date'], '结束日期')

    episode = create_relationship_to(['RadioEpisode', 'TVEpisode', 'Episode'], '剧集')

    numberOfEpisodes = create_relationship_to(['Integer'], '剧集数')

    partOfSeries = create_relationship_to(['MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'CreativeWorkSeries'], '所属系列')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    seasonNumber = create_relationship_to(['Text', 'Integer'], '季的编号')

    startDate = create_relationship_to(['Date'], '开始日期')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class RadioSeason(CreativeWorkSeason):
    pass


class Person(Thing):
    additionalName = create_relationship_to(['Text'], '附加名称')

    address = create_relationship_to(['PostalAddress', 'Text'], '地址')

    affiliation = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '所属机构')

    alumniOf = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '毕业于')

    award = create_relationship_to(['Text'], '所获奖项')

    birthDate = create_relationship_to(['Date'], '出生日期')

    birthPlace = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '出生地点')

    brand = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Brand'], '品牌')

    children = create_relationship_to(['Person'], '子女')

    colleague = create_relationship_to(['Person', 'Text'], '同事')

    contactPoint = create_relationship_to(['PostalAddress', 'ContactPoint'], '联络点')

    deathDate = create_relationship_to(['Date'], '逝世日期')

    deathPlace = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '逝世地点')

    duns = create_relationship_to(['Text'], '邓白氏编码')

    email = create_relationship_to(['Text'], '电子邮件')

    familyName = create_relationship_to(['Text'], '姓')

    faxNumber = create_relationship_to(['Text'], '传真号')

    follows = create_relationship_to(['Person'], '关注')

    funder = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '投资者')

    gender = create_relationship_to(['GenderType', 'Text'], '性别')

    givenName = create_relationship_to(['Text'], '名')

    globalLocationNumber = create_relationship_to(['Text'], '全球位置码')

    hasOfferCatalog = create_relationship_to(['OfferCatalog'], '清单')

    hasPOS = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '销售点')

    height = create_relationship_to(['Distance', 'QuantitativeValue'], '高度')

    homeLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'PostalAddress', 'ContactPoint'], '家庭地址')

    honorificPrefix = create_relationship_to(['Text'], '姓名前面的敬语')

    honorificSuffix = create_relationship_to(['Text'], '姓名后面的敬语')

    isicV4 = create_relationship_to(['Text'], '国际标准行业分类')

    jobTitle = create_relationship_to(['Text'], '工作头衔')

    knows = create_relationship_to(['Person'], '认识')

    makesOffer = create_relationship_to(['AggregateOffer', 'Offer'], '提供的产品或服务')

    memberOf = create_relationship_to(['ProgramMembership', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '会员所属的机构')

    naics = create_relationship_to(['Text'], '北美行业分类系统')

    nationality = create_relationship_to(['Country'], '国籍')

    netWorth = create_relationship_to(['MonetaryAmount', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '净资产')

    owns = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'OwnershipInfo'], '拥有')

    parent = create_relationship_to(['Person'], '父亲或母亲')

    performerIn = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '表演活动')

    publishingPrinciples = create_relationship_to(['Text', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '出版准则')

    relatedTo = create_relationship_to(['Person'], '亲属')

    seeks = create_relationship_to(['Demand'], '用户需求')

    sibling = create_relationship_to(['Person'], '兄弟姐妹')

    sponsor = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '赞助者')

    spouse = create_relationship_to(['Person'], '配偶')

    taxID = create_relationship_to(['Text'], '纳税识别号码')

    telephone = create_relationship_to(['Text'], '电话号码')

    vatID = create_relationship_to(['Text'], '欧盟税号')

    weight = create_relationship_to(['QuantitativeValue'], '重量')

    workLocation = create_relationship_to(['PostalAddress', 'ContactPoint', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '工作地点')

    worksFor = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '受雇于')


class Organization(Thing):
    address = create_relationship_to(['PostalAddress', 'Text'], '地址')

    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    alumni = create_relationship_to(['Person'], '校友')

    areaServed = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea', 'Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '服务覆盖区域')

    award = create_relationship_to(['Text'], '所获奖项')

    brand = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Brand'], '品牌')

    contactPoint = create_relationship_to(['PostalAddress', 'ContactPoint'], '联络点')

    department = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '部门')

    dissolutionDate = create_relationship_to(['Date'], '解散日期')

    duns = create_relationship_to(['Text'], '邓白氏编码')

    email = create_relationship_to(['Text'], '电子邮件')

    employee = create_relationship_to(['Person'], '雇员')

    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')

    faxNumber = create_relationship_to(['Text'], '传真号')

    founder = create_relationship_to(['Person'], '创始人')

    foundingDate = create_relationship_to(['Date'], '成立日期')

    foundingLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '成立地点')

    funder = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '投资者')

    globalLocationNumber = create_relationship_to(['Text'], '全球位置码')

    hasOfferCatalog = create_relationship_to(['OfferCatalog'], '清单')

    hasPOS = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '销售点')

    isicV4 = create_relationship_to(['Text'], '国际标准行业分类')

    legalName = create_relationship_to(['Text'], '官方名称')

    leiCode = create_relationship_to(['Text'], '全球法人机构识别编码')

    location = create_relationship_to(['PostalAddress', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text'], '地点')

    logo = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '商标')

    makesOffer = create_relationship_to(['AggregateOffer', 'Offer'], '提供的产品或服务')

    member = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '会员')

    memberOf = create_relationship_to(['ProgramMembership', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '会员所属的机构')

    naics = create_relationship_to(['Text'], '北美行业分类系统')

    numberOfEmployees = create_relationship_to(['QuantitativeValue'], '雇员数')

    owns = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'OwnershipInfo'], '拥有')

    parentOrganization = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '上级组织')

    publishingPrinciples = create_relationship_to(['Text', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '出版准则')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    seeks = create_relationship_to(['Demand'], '用户需求')

    sponsor = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '赞助者')

    subOrganization = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '子机构')

    taxID = create_relationship_to(['Text'], '纳税识别号码')

    telephone = create_relationship_to(['Text'], '电话号码')

    vatID = create_relationship_to(['Text'], '欧盟税号')


class SportsOrganization(Organization):
    sport = create_relationship_to(['Text'], '运动')


class SportsTeam(SportsOrganization):
    athlete = create_relationship_to(['Person'], '运动员')

    coach = create_relationship_to(['Person'], '教练')


class EducationalOrganization(Organization):
    alumni = create_relationship_to(['Person'], '校友')


class HighSchool(EducationalOrganization):
    pass


class School(EducationalOrganization):
    pass


class ElementarySchool(EducationalOrganization):
    pass


class CollegeOrUniversity(EducationalOrganization):
    pass


class Preschool(EducationalOrganization):
    pass


class MiddleSchool(EducationalOrganization):
    pass


class Airline(Organization):
    boardingPolicy = create_relationship_to(['BoardingPolicyType'], '登机政策')

    iataCode = create_relationship_to(['Text'], '国际航空运输协会代码')


class PerformingGroup(Organization):
    pass


class DanceGroup(PerformingGroup):
    pass


class MusicGroup(PerformingGroup):
    album = create_relationship_to(['MusicAlbum'], '专辑')

    genre = create_relationship_to(['Text'], '风格')

    track = create_relationship_to(['MusicRecording', 'OfferCatalog', 'BreadcrumbList', 'HowToSection', 'HowToStep', 'ItemList'], '音轨')


class TheaterGroup(PerformingGroup):
    pass


class Corporation(Organization):
    tickerSymbol = create_relationship_to(['Text'], '股票代号')


class MedicalOrganization(Organization):
    pass


class Pharmacy(MedicalOrganization):
    pass


class Physician(MedicalOrganization):
    pass


class GovernmentOrganization(Organization):
    pass


class NGO(Organization):
    pass


class Place(Thing):
    additionalProperty = create_relationship_to(['LocationFeatureSpecification', 'PropertyValue'], '附加属性')

    address = create_relationship_to(['PostalAddress', 'Text'], '地址')

    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    amenityFeature = create_relationship_to(['LocationFeatureSpecification'], '特色服务')

    branchCode = create_relationship_to(['Text'], '分支编码')

    containedInPlace = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '包含在')

    containsPlace = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '包含')

    event = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '事件')

    faxNumber = create_relationship_to(['Text'], '传真号')

    geo = create_relationship_to(['GeoCoordinates', 'GeoCircle', 'GeoShape'], '经纬度')

    globalLocationNumber = create_relationship_to(['Text'], '全球位置码')

    hasMap = create_relationship_to(['Text', 'Map'], '地图URL')

    isAccessibleForFree = create_relationship_to(['Bool'], '是否免费')

    isicV4 = create_relationship_to(['Text'], '国际标准行业分类')

    logo = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '商标')

    maximumAttendeeCapacity = create_relationship_to(['Integer'], '最多可容纳多少人参与')

    openingHoursSpecification = create_relationship_to(['OpeningHoursSpecification'], '开放时间详情')

    photo = create_relationship_to(['Barcode', 'ImageObject', 'Photograph'], '照片')

    publicAccess = create_relationship_to(['Bool'], '是否对公众开放')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    smokingAllowed = create_relationship_to(['Bool'], '是否允许吸烟')

    specialOpeningHoursSpecification = create_relationship_to(['OpeningHoursSpecification'], '特殊开放时间详情')

    telephone = create_relationship_to(['Text'], '电话号码')


class Accommodation(Place):
    amenityFeature = create_relationship_to(['LocationFeatureSpecification'], '特色服务')

    floorSize = create_relationship_to(['QuantitativeValue'], '建筑面积')

    numberOfRooms = create_relationship_to(['QuantitativeValue', 'Integer'], '房间数')

    permittedUsage = create_relationship_to(['Text'], '允许的用途')

    petsAllowed = create_relationship_to(['Text', 'Bool'], '是否允许带宠物')


class Suite(Accommodation):
    bed = create_relationship_to(['Text', 'BedDetails'], '床位信息')

    numberOfRooms = create_relationship_to(['QuantitativeValue', 'Integer'], '房间数')

    occupancy = create_relationship_to(['QuantitativeValue'], '最大入住人数')


class Room(Accommodation):
    pass


class HotelRoom(Room):
    bed = create_relationship_to(['Text', 'BedDetails'], '床位信息')

    occupancy = create_relationship_to(['QuantitativeValue'], '最大入住人数')


class MeetingRoom(Room):
    pass


class House(Accommodation):
    numberOfRooms = create_relationship_to(['QuantitativeValue', 'Integer'], '房间数')


class SingleFamilyResidence(House):
    numberOfRooms = create_relationship_to(['QuantitativeValue', 'Integer'], '房间数')

    occupancy = create_relationship_to(['QuantitativeValue'], '最大入住人数')


class Apartment(Accommodation):
    numberOfRooms = create_relationship_to(['QuantitativeValue', 'Integer'], '房间数')

    occupancy = create_relationship_to(['QuantitativeValue'], '最大入住人数')


class CampingPitch(Accommodation):
    pass


class LandmarksOrHistoricalBuildings(Place):
    pass


class TouristAttraction(Place):
    availableLanguage = create_relationship_to(['Language', 'Text'], '支持的语言')

    touristType = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience', 'Text'], '适宜的游客类型')


class CivicStructure(Place):
    openingHours = create_relationship_to(['Text'], '开放时间')


class EventVenue(CivicStructure):
    pass


class Museum(CivicStructure):
    pass


class Zoo(CivicStructure):
    pass


class PlaceOfWorship(CivicStructure):
    pass


class Synagogue(PlaceOfWorship):
    pass


class HinduTemple(PlaceOfWorship):
    pass


class Church(PlaceOfWorship):
    pass


class BuddhistTemple(PlaceOfWorship):
    pass


class Mosque(PlaceOfWorship):
    pass


class CatholicChurch(PlaceOfWorship):
    pass


class Crematorium(CivicStructure):
    pass


class Playground(CivicStructure):
    pass


class ParkingFacility(CivicStructure):
    pass


class Aquarium(CivicStructure):
    pass


class Bridge(CivicStructure):
    pass


class TrainStation(CivicStructure):
    pass


class Beach(CivicStructure):
    pass


class Park(CivicStructure):
    pass


class GovernmentBuilding(CivicStructure):
    pass


class Embassy(GovernmentBuilding):
    pass


class DefenceEstablishment(GovernmentBuilding):
    pass


class LegislativeBuilding(GovernmentBuilding):
    pass


class CityHall(GovernmentBuilding):
    pass


class Courthouse(GovernmentBuilding):
    pass


class PerformingArtsTheater(CivicStructure):
    pass


class TaxiStand(CivicStructure):
    pass


class MusicVenue(CivicStructure):
    pass


class BusStop(CivicStructure):
    pass


class SubwayStation(CivicStructure):
    pass


class RVPark(CivicStructure):
    pass


class Cemetery(CivicStructure):
    pass


class Airport(CivicStructure):
    iataCode = create_relationship_to(['Text'], '国际航空运输协会代码')

    icaoCode = create_relationship_to(['Text'], '国际民航组织机场代码')


class BusStation(CivicStructure):
    pass


class Residence(Place):
    pass


class ApartmentComplex(Residence):
    pass


class GatedResidenceCommunity(Residence):
    pass


class Landform(Place):
    pass


class Volcano(Landform):
    pass


class Continent(Landform):
    pass


class Mountain(Landform):
    pass


class BodyOfWater(Landform):
    pass


class SeaBodyOfWater(BodyOfWater):
    pass


class Reservoir(BodyOfWater):
    pass


class RiverBodyOfWater(BodyOfWater):
    pass


class Waterfall(BodyOfWater):
    pass


class LakeBodyOfWater(BodyOfWater):
    pass


class OceanBodyOfWater(BodyOfWater):
    pass


class Canal(BodyOfWater):
    pass


class Pond(BodyOfWater):
    pass


class AdministrativeArea(Place):
    pass


class Country(AdministrativeArea):
    pass


class State(AdministrativeArea):
    pass


class City(AdministrativeArea):
    pass


class Intangible(Thing):
    pass


class Demand(Intangible):
    acceptedPaymentMethod = create_relationship_to(['PaymentCard', 'CreditCard', 'PaymentMethod', 'LoanOrCredit'], '卖家接受的支付方式')

    advanceBookingRequirement = create_relationship_to(['QuantitativeValue'], '预定要求')

    areaServed = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea', 'Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '服务覆盖区域')

    availability = create_relationship_to(['ItemAvailability'], '供应状态')

    availabilityEnds = create_relationship_to(['Date'], '供应截止时间')

    availabilityStarts = create_relationship_to(['Date'], '供应开始时间')

    availableAtOrFrom = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '报价地点')

    availableDeliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '支持的物流方式')

    businessFunction = create_relationship_to(['BusinessFunction'], '商业职能')

    deliveryLeadTime = create_relationship_to(['QuantitativeValue'], '物流送货时间')

    eligibleCustomerType = create_relationship_to(['BusinessEntityType'], '适用的顾客类型')

    eligibleDuration = create_relationship_to(['QuantitativeValue'], '有效时间')

    eligibleQuantity = create_relationship_to(['QuantitativeValue'], '适用数量')

    eligibleRegion = create_relationship_to(['Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '适用地区')

    eligibleTransactionVolume = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '适用购买数量')

    gtin12 = create_relationship_to(['Text'], '12位全球贸易品项识别码')

    gtin13 = create_relationship_to(['Text'], '13位全球贸易品项识别码')

    gtin14 = create_relationship_to(['Text'], '14位全球贸易品项识别码')

    gtin8 = create_relationship_to(['Text'], '8位全球贸易品项识别码')

    includesObject = create_relationship_to(['TypeAndQuantityNode'], '包含对象')

    ineligibleRegion = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text', 'GeoCircle', 'GeoShape'], '不适用地区')

    inventoryLevel = create_relationship_to(['QuantitativeValue'], '库存量')

    itemCondition = create_relationship_to(['OfferItemCondition'], '规格')

    itemOffered = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '销售物品')

    mpn = create_relationship_to(['Text'], '制造商零件编码')

    priceSpecification = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '价格明细')

    seller = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '卖家')

    serialNumber = create_relationship_to(['Text'], '序列号')

    sku = create_relationship_to(['Text'], '单品编号')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validThrough = create_relationship_to(['Date'], '有效截止日期')

    warranty = create_relationship_to(['WarrantyPromise'], '担保')


class Rating(Intangible):
    author = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '作者')

    bestRating = create_relationship_to(['Integer', 'Text'], '支持的最高评分分数')

    ratingValue = create_relationship_to(['Integer', 'Text'], '评分')

    worstRating = create_relationship_to(['Integer', 'Text'], '评价系统的最低评分')


class AggregateRating(Rating):
    itemReviewed = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '评价物品')

    ratingCount = create_relationship_to(['Integer'], '评分总数')

    reviewCount = create_relationship_to(['Integer'], '评论的总数')


class Trip(Intangible):
    arrivalTime = create_relationship_to(['Date'], '到达时间')

    departureTime = create_relationship_to(['Date'], '出发时间')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')

    provider = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '提供方')


class BusTrip(Trip):
    arrivalBusStop = create_relationship_to(['BusStation', 'BusStop'], '到达汽车站')

    busName = create_relationship_to(['Text'], '公共汽车名称')

    busNumber = create_relationship_to(['Text'], '公共汽车编号')

    departureBusStop = create_relationship_to(['BusStation', 'BusStop'], '出发汽车站')


class Flight(Trip):
    aircraft = create_relationship_to(['Car', 'Vehicle', 'Text'], '航空器')

    arrivalAirport = create_relationship_to(['Airport'], '到达机场')

    arrivalGate = create_relationship_to(['Text'], '到达登机口')

    arrivalTerminal = create_relationship_to(['Text'], '到达航站楼')

    boardingPolicy = create_relationship_to(['BoardingPolicyType'], '登机政策')

    departureAirport = create_relationship_to(['Airport'], '出发机场')

    departureGate = create_relationship_to(['Text'], '出发登机口')

    departureTerminal = create_relationship_to(['Text'], '出发航站楼')

    estimatedFlightDuration = create_relationship_to(['Duration', 'Text'], '预计飞行时间')

    flightDistance = create_relationship_to(['Distance', 'Text'], '飞行距离')

    flightNumber = create_relationship_to(['Text'], '航班号')

    mealService = create_relationship_to(['Text'], '套餐描述')

    seller = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '卖家')

    webCheckinTime = create_relationship_to(['Date'], '网上值机时间')


class TrainTrip(Trip):
    arrivalPlatform = create_relationship_to(['Text'], '到达站台')

    arrivalStation = create_relationship_to(['TrainStation'], '到达火车站')

    departurePlatform = create_relationship_to(['Text'], '出发站台')

    departureStation = create_relationship_to(['TrainStation'], '出发火车站')

    trainName = create_relationship_to(['Text'], '火车名称')

    trainNumber = create_relationship_to(['Text'], '火车编号')


class PropertyValueSpecification(Intangible):
    defaultValue = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '缺省值')

    maxValue = create_relationship_to(['Integer'], '最大值')

    minValue = create_relationship_to(['Integer'], '最小值')

    multipleValues = create_relationship_to(['Bool'], '是否允许多个值')

    readonlyValue = create_relationship_to(['Bool'], '值是否只读')

    stepValue = create_relationship_to(['Integer'], '步长')

    valueMaxLength = create_relationship_to(['Integer'], '值的最大长度')

    valueMinLength = create_relationship_to(['Integer'], '值的最小长度')

    valueName = create_relationship_to(['Text'], '值的名称')

    valuePattern = create_relationship_to(['Text'], '值的正则表达式验证模版')

    valueRequired = create_relationship_to(['Bool'], '值是否必须')


class ProgramMembership(Intangible):
    hostingOrganization = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '会员服务提供者')

    member = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '会员')

    membershipNumber = create_relationship_to(['Text'], '会员编号')

    programName = create_relationship_to(['Text'], '会员身份的折扣计划')


class MenuItem(Intangible):
    nutrition = create_relationship_to(['NutritionInformation'], '营养成分')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')

    suitableForDiet = create_relationship_to(['RestrictedDiet'], '适用的饮食')


class EntryPoint(Intangible):
    actionApplication = create_relationship_to(['VideoGame', 'WebApplication', 'MobileApplication', 'SoftwareApplication'], '执行操作的应用')

    actionPlatform = create_relationship_to(['Text'], '执行操作的平台')

    contentType = create_relationship_to(['Text'], '内容的文件类型')

    encodingType = create_relationship_to(['Text'], '编码类型')

    httpMethod = create_relationship_to(['Text'], 'http方法')

    urlTemplate = create_relationship_to(['Text'], '链接模版')


class DigitalDocumentPermission(Intangible):
    grantee = create_relationship_to(['PostalAddress', 'ContactPoint', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience', 'Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '受让人')

    permissionType = create_relationship_to(['DigitalDocumentPermissionType'], '权限类型')


class GameServer(Intangible):
    game = create_relationship_to(['VideoGame'], '游戏')

    playersOnline = create_relationship_to(['Integer'], '在线玩家数')

    serverStatus = create_relationship_to(['GameServerStatus'], '服务器状态')


class Audience(Intangible):
    audienceType = create_relationship_to(['Text'], '受众类型')

    geographicArea = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea'], '受众群所在地理区域')


class EducationalAudience(Audience):
    educationalRole = create_relationship_to(['Text'], '教育活动中的角色')


class PeopleAudience(Audience):
    requiredGender = create_relationship_to(['Text'], '性别要求')

    requiredMaxAge = create_relationship_to(['Integer'], '最大年龄要求')

    requiredMinAge = create_relationship_to(['Integer'], '最小年龄要求')

    suggestedGender = create_relationship_to(['Text'], '建议的受众性别')

    suggestedMaxAge = create_relationship_to(['Integer'], '建议的受众最大年龄')

    suggestedMinAge = create_relationship_to(['Integer'], '建议的受众最小年龄')


class ParentAudience(PeopleAudience):
    childMaxAge = create_relationship_to(['Integer'], '最大儿童年龄')

    childMinAge = create_relationship_to(['Integer'], '最小儿童年龄')


class BusinessAudience(Audience):
    numberOfEmployees = create_relationship_to(['QuantitativeValue'], '雇员数')

    yearlyRevenue = create_relationship_to(['QuantitativeValue'], '年营业额')

    yearsInOperation = create_relationship_to(['QuantitativeValue'], '运营年数')


class ComputerLanguage(Intangible):
    pass


class ListItem(Intangible):
    item = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '条目')

    nextItem = create_relationship_to(['HowToDirection', 'HowToItem', 'HowToSupply', 'HowToTool', 'HowToSection', 'HowToStep', 'HowToTip', 'ListItem'], '下一项')

    position = create_relationship_to(['Text', 'Integer'], '位置')

    previousItem = create_relationship_to(['HowToDirection', 'HowToItem', 'HowToSupply', 'HowToTool', 'HowToSection', 'HowToStep', 'HowToTip', 'ListItem'], '上一条目')


class HowToItem(ListItem):
    requiredQuantity = create_relationship_to(['Text', 'QuantitativeValue', 'Integer'], '相关物料的数量')


class HowToSupply(HowToItem):
    estimatedCost = create_relationship_to(['MonetaryAmount', 'Text'], '相关物料的估价')


class HowToTool(HowToItem):
    pass


class StructuredValue(Intangible):
    pass


class NutritionInformation(StructuredValue):
    calories = create_relationship_to(['Energy'], '卡路里')

    carbohydrateContent = create_relationship_to(['Mass'], '碳水化合物含量')

    cholesterolContent = create_relationship_to(['Mass'], '胆固醇含量')

    fatContent = create_relationship_to(['Mass'], '脂肪含量')

    fiberContent = create_relationship_to(['Mass'], '纤维含量')

    proteinContent = create_relationship_to(['Mass'], '蛋白质含量')

    saturatedFatContent = create_relationship_to(['Mass'], '饱和脂肪含量')

    servingSize = create_relationship_to(['Text'], '食用分量')

    sodiumContent = create_relationship_to(['Mass'], '钠含量')

    sugarContent = create_relationship_to(['Mass'], '糖含量')

    transFatContent = create_relationship_to(['Mass'], '反式脂肪含量')

    unsaturatedFatContent = create_relationship_to(['Mass'], '不饱和脂肪含量')


class PriceSpecification(StructuredValue):
    eligibleQuantity = create_relationship_to(['QuantitativeValue'], '适用数量')

    eligibleTransactionVolume = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '适用购买数量')

    maxPrice = create_relationship_to(['Integer'], '最高价格')

    minPrice = create_relationship_to(['Integer'], '最低价格')

    price = create_relationship_to(['Integer', 'Text'], '价格')

    priceCurrency = create_relationship_to(['Text'], '价格对应的货币单位')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validThrough = create_relationship_to(['Date'], '有效截止日期')

    valueAddedTaxIncluded = create_relationship_to(['Bool'], '是否含税')


class DeliveryChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '适用的送货方式')

    areaServed = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea', 'Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '服务覆盖区域')

    eligibleRegion = create_relationship_to(['Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '适用地区')

    ineligibleRegion = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text', 'GeoCircle', 'GeoShape'], '不适用地区')


class UnitPriceSpecification(PriceSpecification):
    billingIncrement = create_relationship_to(['Integer'], '计费增量')

    priceType = create_relationship_to(['Text'], '价格类型')

    referenceQuantity = create_relationship_to(['QuantitativeValue'], '参考数量')

    unitCode = create_relationship_to(['Text'], '单位代码')

    unitText = create_relationship_to(['Text'], '单位文字')


class CompoundPriceSpecification(PriceSpecification):
    priceComponent = create_relationship_to(['UnitPriceSpecification'], '复合价格中提及的所有单价')


class PaymentChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '适用的送货方式')

    appliesToPaymentMethod = create_relationship_to(['PaymentCard', 'CreditCard', 'PaymentMethod'], '适用的支付方式')


class PropertyValue(StructuredValue):
    maxValue = create_relationship_to(['Integer'], '最大值')

    minValue = create_relationship_to(['Integer'], '最小值')

    propertyID = create_relationship_to(['Text'], '属性ID')

    unitCode = create_relationship_to(['Text'], '单位代码')

    unitText = create_relationship_to(['Text'], '单位文字')

    value = create_relationship_to(['Integer', 'Bool', 'Text', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'StructuredValue'], '值')

    valueReference = create_relationship_to(['EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentCard', 'CreditCard', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'Enumeration', 'QuantitativeValue', 'LocationFeatureSpecification', 'PropertyValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'StructuredValue'], '参考值')


class LocationFeatureSpecification(PropertyValue):
    hoursAvailable = create_relationship_to(['OpeningHoursSpecification'], '服务时间')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validThrough = create_relationship_to(['Date'], '有效截止日期')


class GeoShape(StructuredValue):
    address = create_relationship_to(['PostalAddress', 'Text'], '地址')

    addressCountry = create_relationship_to(['Country', 'Text'], '地址所在国家')

    box = create_relationship_to(['Text'], '边界框')

    circle = create_relationship_to(['Text'], '圆形区域')

    elevation = create_relationship_to(['Text', 'Integer'], '海拔高度')

    line = create_relationship_to(['Text'], '直线')

    polygon = create_relationship_to(['Text'], '多边形')

    postalCode = create_relationship_to(['Text'], '邮政编码')


class GeoCircle(GeoShape):
    geoMidpoint = create_relationship_to(['GeoCoordinates'], '中心点经纬度')

    geoRadius = create_relationship_to(['Distance', 'Integer', 'Text'], '区域半径')


class InteractionCounter(StructuredValue):
    interactionService = create_relationship_to(['WebSite', 'VideoGame', 'WebApplication', 'MobileApplication', 'SoftwareApplication'], '交互对应的软件服务')

    interactionType = create_relationship_to(['AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'Action'], '交互类型')

    userInteractionCount = create_relationship_to(['Integer'], '用户交互数')


class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood = create_relationship_to(['Integer'], '货物数量')

    businessFunction = create_relationship_to(['BusinessFunction'], '商业职能')

    typeOfGood = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '货物类型')

    unitCode = create_relationship_to(['Text'], '单位代码')

    unitText = create_relationship_to(['Text'], '单位文字')


class DatedMoneySpecification(StructuredValue):
    amount = create_relationship_to(['MonetaryAmount', 'Integer'], '金钱数量')

    currency = create_relationship_to(['Text'], '货币种类')

    endDate = create_relationship_to(['Date'], '结束日期')

    startDate = create_relationship_to(['Date'], '开始日期')


class ContactPoint(StructuredValue):
    areaServed = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea', 'Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '服务覆盖区域')

    availableLanguage = create_relationship_to(['Language', 'Text'], '支持的语言')

    contactOption = create_relationship_to(['ContactPointOption'], '联系选项')

    contactType = create_relationship_to(['Text'], '联系方式职能类型')

    email = create_relationship_to(['Text'], '电子邮件')

    faxNumber = create_relationship_to(['Text'], '传真号')

    hoursAvailable = create_relationship_to(['OpeningHoursSpecification'], '服务时间')

    productSupported = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'Text'], '支持的产品')

    telephone = create_relationship_to(['Text'], '电话号码')


class PostalAddress(ContactPoint):
    addressCountry = create_relationship_to(['Country', 'Text'], '地址所在国家')

    addressLocality = create_relationship_to(['Text'], '地址所在地方')

    addressRegion = create_relationship_to(['Text'], '地址所在行政区')

    postOfficeBoxNumber = create_relationship_to(['Text'], '邮政邮箱编号')

    postalCode = create_relationship_to(['Text'], '邮政编码')

    streetAddress = create_relationship_to(['Text'], '街道地址')


class WarrantyPromise(StructuredValue):
    durationOfWarranty = create_relationship_to(['QuantitativeValue'], '保修期')

    warrantyScope = create_relationship_to(['WarrantyScope'], '担保范围')


class MonetaryAmount(StructuredValue):
    currency = create_relationship_to(['Text'], '货币种类')

    maxValue = create_relationship_to(['Integer'], '最大值')

    minValue = create_relationship_to(['Integer'], '最小值')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validThrough = create_relationship_to(['Date'], '有效截止日期')

    value = create_relationship_to(['Integer', 'Bool', 'Text', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'StructuredValue'], '值')


class EngineSpecification(StructuredValue):
    fuelType = create_relationship_to(['Text', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '燃料类型')


class OpeningHoursSpecification(StructuredValue):
    closes = create_relationship_to(['Date'], '关门时间')

    dayOfWeek = create_relationship_to(['DayOfWeek'], '星期几')

    opens = create_relationship_to(['Date'], '开门时间')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validThrough = create_relationship_to(['Date'], '有效截止日期')


class QuantitativeValue(StructuredValue):
    additionalProperty = create_relationship_to(['LocationFeatureSpecification', 'PropertyValue'], '附加属性')

    maxValue = create_relationship_to(['Integer'], '最大值')

    minValue = create_relationship_to(['Integer'], '最小值')

    unitCode = create_relationship_to(['Text'], '单位代码')

    unitText = create_relationship_to(['Text'], '单位文字')

    value = create_relationship_to(['Integer', 'Bool', 'Text', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'StructuredValue'], '值')

    valueReference = create_relationship_to(['EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentCard', 'CreditCard', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'Enumeration', 'QuantitativeValue', 'LocationFeatureSpecification', 'PropertyValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'StructuredValue'], '参考值')


class OwnershipInfo(StructuredValue):
    acquiredFrom = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '获取来源')

    ownedFrom = create_relationship_to(['Date'], '所有权开始时间')

    ownedThrough = create_relationship_to(['Date'], '所有权结束时间')

    typeOfGood = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '货物类型')


class GeoCoordinates(StructuredValue):
    address = create_relationship_to(['PostalAddress', 'Text'], '地址')

    addressCountry = create_relationship_to(['Country', 'Text'], '地址所在国家')

    elevation = create_relationship_to(['Text', 'Integer'], '海拔高度')

    latitude = create_relationship_to(['Text', 'Integer'], '纬度')

    longitude = create_relationship_to(['Text', 'Integer'], '经度')

    postalCode = create_relationship_to(['Text'], '邮政编码')


class AlignmentObject(Intangible):
    alignmentType = create_relationship_to(['Text'], '教学达标类型')

    educationalFramework = create_relationship_to(['Text'], '对应的教学标准')

    targetDescription = create_relationship_to(['Text'], '目标知识点的描述')

    targetName = create_relationship_to(['Text'], '目标知识点的名称')

    targetUrl = create_relationship_to(['Text'], '目标知识点的链接')


class BroadcastChannel(Intangible):
    broadcastChannelId = create_relationship_to(['Text'], '广播频道ID')

    broadcastServiceTier = create_relationship_to(['Text'], '广播频道所属的服务级别')

    genre = create_relationship_to(['Text'], '风格')

    inBroadcastLineup = create_relationship_to(['CableOrSatelliteService'], '提供该频道的有线或者卫星服务')

    providesBroadcastService = create_relationship_to(['BroadcastService'], '提供的广播服务')


class TelevisionChannel(BroadcastChannel):
    pass


class RadioChannel(BroadcastChannel):
    pass


class Permit(Intangible):
    issuedBy = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '许可的签发机构')

    issuedThrough = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service'], '被许可的服务')

    permitAudience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '许可证的受众群')

    validFor = create_relationship_to(['Duration'], '有效时间')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validIn = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea'], '有效地区')

    validUntil = create_relationship_to(['Date'], '失效日期')


class GovernmentPermit(Permit):
    pass


class DataFeedItem(Intangible):
    dateCreated = create_relationship_to(['Date'], '创建日期')

    dateDeleted = create_relationship_to(['Date'], '删除日期')

    dateModified = create_relationship_to(['Date'], '更新日期')

    item = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '条目')


class ServiceChannel(Intangible):
    availableLanguage = create_relationship_to(['Language', 'Text'], '支持的语言')

    processingTime = create_relationship_to(['Duration'], '处理时间')

    providesService = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service'], '提供的服务')

    serviceLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '服务所在地点')

    servicePhone = create_relationship_to(['PostalAddress', 'ContactPoint'], '服务电话')

    servicePostalAddress = create_relationship_to(['PostalAddress'], '服务邮寄地址')

    serviceSmsNumber = create_relationship_to(['PostalAddress', 'ContactPoint'], '服务短信号码')

    serviceUrl = create_relationship_to(['Text'], '服务链接')


class Order(Intangible):
    acceptedOffer = create_relationship_to(['AggregateOffer', 'Offer'], '被接受的报价')

    billingAddress = create_relationship_to(['PostalAddress'], '账单地址')

    broker = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '经纪人')

    confirmationNumber = create_relationship_to(['Text'], '确认编号')

    customer = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '顾客')

    discount = create_relationship_to(['Text', 'Integer'], '折扣')

    discountCode = create_relationship_to(['Text'], '优惠码')

    discountCurrency = create_relationship_to(['Text'], '折扣对应的货币')

    isGift = create_relationship_to(['Bool'], '是否礼物')

    orderDate = create_relationship_to(['Date'], '订单的下单日期')

    orderDelivery = create_relationship_to(['ParcelDelivery'], '订单的物流选择')

    orderNumber = create_relationship_to(['Text'], '订单的编号')

    orderStatus = create_relationship_to(['OrderStatus'], '订单的状态')

    orderedItem = create_relationship_to(['OrderItem', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '订单条目')

    partOfInvoice = create_relationship_to(['Invoice'], '所属账单')

    paymentDueDate = create_relationship_to(['Date'], '最晚付款日期')

    paymentMethod = create_relationship_to(['PaymentCard', 'CreditCard', 'PaymentMethod'], '支付方式')

    paymentMethodId = create_relationship_to(['Text'], '支付方式ID')

    paymentUrl = create_relationship_to(['Text'], '付款链接')

    seller = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '卖家')


class Series(Intangible):
    pass


class Quantity(Intangible):
    pass


class Mass(Quantity):
    pass


class Energy(Quantity):
    pass


class Duration(Quantity):
    pass


class Distance(Quantity):
    pass


class Brand(Intangible):
    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    logo = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '商标')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')


class Role(Intangible):
    endDate = create_relationship_to(['Date'], '结束日期')

    roleName = create_relationship_to(['Text'], '角色名称')

    startDate = create_relationship_to(['Date'], '开始日期')


class PerformanceRole(Role):
    characterName = create_relationship_to(['Text'], '人物角色名字')


class OrganizationRole(Role):
    numberedPosition = create_relationship_to(['Integer'], '角色编码')


class EmployeeRole(OrganizationRole):
    baseSalary = create_relationship_to(['Integer', 'MonetaryAmount', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '底薪')

    salaryCurrency = create_relationship_to(['Text'], '工资结算货币')


class ItemList(Intangible):
    itemListElement = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing', 'Text'], '列表里的项目元素')

    itemListOrder = create_relationship_to(['Text', 'ItemListOrderType'], '列表排列顺序')

    numberOfItems = create_relationship_to(['Integer'], '条目数量')


class BreadcrumbList(ItemList):
    pass


class OfferCatalog(ItemList):
    pass


class Seat(Intangible):
    seatNumber = create_relationship_to(['Text'], '座位编号')

    seatRow = create_relationship_to(['Text'], '座位排号')

    seatSection = create_relationship_to(['Text'], '座位区号')

    seatingType = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue', 'Text'], '座位类型')


class Ticket(Intangible):
    dateIssued = create_relationship_to(['Date'], '签发日期')

    issuedBy = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '许可的签发机构')

    priceCurrency = create_relationship_to(['Text'], '价格对应的货币单位')

    ticketNumber = create_relationship_to(['Text'], '票据编号')

    ticketToken = create_relationship_to(['Text'], '票据的二维码或条形码')

    ticketedSeat = create_relationship_to(['Seat'], '票据对应的座位')

    totalPrice = create_relationship_to(['Integer', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification', 'Text'], '总价')

    underName = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '持票人')


class Invoice(Intangible):
    accountId = create_relationship_to(['Text'], '账户ID')

    billingPeriod = create_relationship_to(['Duration'], '账单结算周期')

    broker = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '经纪人')

    category = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '类别')

    confirmationNumber = create_relationship_to(['Text'], '确认编号')

    customer = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '顾客')

    minimumPaymentDue = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification', 'MonetaryAmount'], '最小付款额')

    paymentDueDate = create_relationship_to(['Date'], '最晚付款日期')

    paymentMethod = create_relationship_to(['PaymentCard', 'CreditCard', 'PaymentMethod'], '支付方式')

    paymentMethodId = create_relationship_to(['Text'], '支付方式ID')

    paymentStatus = create_relationship_to(['PaymentStatusType', 'Text'], '支付状态')

    provider = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '提供方')

    referencesOrder = create_relationship_to(['Order'], '对应的订单')

    scheduledPaymentDate = create_relationship_to(['Date'], '预约的付款日期')

    totalPaymentDue = create_relationship_to(['MonetaryAmount', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '应付款总额')


class OrderItem(Intangible):
    orderDelivery = create_relationship_to(['ParcelDelivery'], '订单的物流选择')

    orderItemNumber = create_relationship_to(['Text'], '订单条目的编号')

    orderItemStatus = create_relationship_to(['OrderStatus'], '订单条目的状态')

    orderQuantity = create_relationship_to(['Integer'], '订单条目的采购数量')

    orderedItem = create_relationship_to(['OrderItem', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '订单条目')


class Service(Intangible):
    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    areaServed = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea', 'Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '服务覆盖区域')

    audience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '受众')

    availableChannel = create_relationship_to(['ServiceChannel'], '获得服务的渠道')

    award = create_relationship_to(['Text'], '所获奖项')

    brand = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Brand'], '品牌')

    broker = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '经纪人')

    category = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '类别')

    hasOfferCatalog = create_relationship_to(['OfferCatalog'], '清单')

    hoursAvailable = create_relationship_to(['OpeningHoursSpecification'], '服务时间')

    isRelatedTo = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service'], '相关')

    isSimilarTo = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '相似')

    logo = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '商标')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')

    provider = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '提供方')

    providerMobility = create_relationship_to(['Text'], '提供方是否机动')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    serviceOutput = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '服务产出')

    serviceType = create_relationship_to(['Text'], '服务类型')


class FoodService(Service):
    pass


class FinancialProduct(Service):
    annualPercentageRate = create_relationship_to(['QuantitativeValue', 'Integer'], '年利率')

    feesAndCommissionsSpecification = create_relationship_to(['Text'], '费用和佣金详情')

    interestRate = create_relationship_to(['Integer', 'QuantitativeValue'], '利率')


class BankAccount(FinancialProduct):
    pass


class PaymentService(FinancialProduct):
    pass


class InvestmentOrDeposit(FinancialProduct):
    amount = create_relationship_to(['MonetaryAmount', 'Integer'], '金钱数量')


class LoanOrCredit(FinancialProduct):
    amount = create_relationship_to(['MonetaryAmount', 'Integer'], '金钱数量')

    loanTerm = create_relationship_to(['QuantitativeValue'], '贷款期限')

    requiredCollateral = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '必须抵押品')


class CurrencyConversionService(FinancialProduct):
    pass


class CableOrSatelliteService(Service):
    pass


class BroadcastService(Service):
    broadcastAffiliateOf = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '所属广播站')

    broadcastDisplayName = create_relationship_to(['Text'], '广播频道名称')

    broadcastTimezone = create_relationship_to(['Text'], '广播频道所在的时区')

    broadcaster = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '广播频道的提供商')

    parentService = create_relationship_to(['BroadcastService'], '上级服务')

    videoFormat = create_relationship_to(['Text'], '视频格式')


class TaxiService(Service):
    pass


class Taxi(Service):
    pass


class GovernmentService(Service):
    serviceOperator = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '服务的运营商')


class Enumeration(Intangible):
    pass


class GenderType(Enumeration):
    pass


class MapCategoryType(Enumeration):
    pass


class ContactPointOption(Enumeration):
    pass


class DigitalDocumentPermissionType(Enumeration):
    pass


class PaymentStatusType(Enumeration):
    pass


class MusicAlbumReleaseType(Enumeration):
    pass


class GameServerStatus(Enumeration):
    pass


class OfferItemCondition(Enumeration):
    pass


class RestrictedDiet(Enumeration):
    pass


class QualitativeValue(Enumeration):
    additionalProperty = create_relationship_to(['LocationFeatureSpecification', 'PropertyValue'], '附加属性')

    equal = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '等于')

    greater = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '大于')

    greaterOrEqual = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '大于等于')

    lesser = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '小于')

    lesserOrEqual = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '小于等于')

    nonEqual = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '不等于')

    valueReference = create_relationship_to(['EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentCard', 'CreditCard', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'Enumeration', 'QuantitativeValue', 'LocationFeatureSpecification', 'PropertyValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'StructuredValue'], '参考值')


class SteeringPositionValue(QualitativeValue):
    pass


class DriveWheelConfigurationValue(QualitativeValue):
    pass


class PaymentMethod(Enumeration):
    pass


class ActionStatusType(Enumeration):
    pass


class OrderStatus(Enumeration):
    pass


class BookFormatType(Enumeration):
    pass


class ItemListOrderType(Enumeration):
    pass


class WarrantyScope(Enumeration):
    pass


class DeliveryMethod(Enumeration):
    pass


class ParcelService(DeliveryMethod):
    pass


class LockerDelivery(DeliveryMethod):
    pass


class MusicAlbumProductionType(Enumeration):
    pass


class Specialty(Enumeration):
    pass


class ItemAvailability(Enumeration):
    pass


class BusinessFunction(Enumeration):
    pass


class RsvpResponseType(Enumeration):
    pass


class DayOfWeek(Enumeration):
    pass


class BusinessEntityType(Enumeration):
    pass


class ReservationStatusType(Enumeration):
    pass


class BoardingPolicyType(Enumeration):
    pass


class MusicReleaseFormatType(Enumeration):
    pass


class EventStatusType(Enumeration):
    pass


class GamePlayMode(Enumeration):
    pass


class BedDetails(Intangible):
    numberOfBeds = create_relationship_to(['Integer'], '床位数')

    typeOfBed = create_relationship_to(['Text'], '床位类型')


class Language(Intangible):
    pass


class ParcelDelivery(Intangible):
    deliveryAddress = create_relationship_to(['PostalAddress'], '物流送货地址')

    deliveryStatus = create_relationship_to(['DeliveryEvent'], '物流送货状态')

    expectedArrivalFrom = create_relationship_to(['Date'], '预计最早送达时间')

    expectedArrivalUntil = create_relationship_to(['Date'], '预计最晚送达时间')

    hasDeliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '物流送货方式')

    itemShipped = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '运送物品')

    originAddress = create_relationship_to(['PostalAddress'], '发货者的地址')

    partOfOrder = create_relationship_to(['Order'], '所属订单')

    provider = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '提供方')

    trackingNumber = create_relationship_to(['Text'], '运单号')

    trackingUrl = create_relationship_to(['Text'], '物流状态跟踪链接')


class JobPosting(Intangible):
    baseSalary = create_relationship_to(['Integer', 'MonetaryAmount', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '底薪')

    datePosted = create_relationship_to(['Date'], '发布日期')

    educationRequirements = create_relationship_to(['Text'], '教育背景要求')

    employmentType = create_relationship_to(['Text'], '就业类型')

    experienceRequirements = create_relationship_to(['Text'], '经验要求')

    hiringOrganization = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '招聘机构')

    incentiveCompensation = create_relationship_to(['Text'], '奖金补贴')

    industry = create_relationship_to(['Text'], '所属行业')

    jobBenefits = create_relationship_to(['Text'], '职位福利')

    jobLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '工作地点')

    occupationalCategory = create_relationship_to(['Text'], '职位分类')

    qualifications = create_relationship_to(['Text'], '资历要求')

    responsibilities = create_relationship_to(['Text'], '工作职责')

    salaryCurrency = create_relationship_to(['Text'], '工资结算货币')

    skills = create_relationship_to(['Text'], '技能要求')

    specialCommitments = create_relationship_to(['Text'], '特别承诺')

    title = create_relationship_to(['Text'], '头衔')

    validThrough = create_relationship_to(['Date'], '有效截止日期')

    workHours = create_relationship_to(['Text'], '工作时间')


class Reservation(Intangible):
    bookingTime = create_relationship_to(['Date'], '预订时间')

    broker = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '经纪人')

    modifiedTime = create_relationship_to(['Date'], '更新时间')

    priceCurrency = create_relationship_to(['Text'], '价格对应的货币单位')

    programMembershipUsed = create_relationship_to(['ProgramMembership'], '使用的会员身份')

    provider = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '提供方')

    reservationFor = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '预定的对象')

    reservationId = create_relationship_to(['Text'], '预定的ID')

    reservationStatus = create_relationship_to(['ReservationStatusType'], '预定的状态')

    reservedTicket = create_relationship_to(['Ticket'], '预定的票据')

    totalPrice = create_relationship_to(['Integer', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification', 'Text'], '总价')

    underName = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '持票人')


class TaxiReservation(Reservation):
    partySize = create_relationship_to(['Integer', 'QuantitativeValue'], '预约活动的参与人数')

    pickupLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '接人地点')

    pickupTime = create_relationship_to(['Date'], '接人时间')


class ReservationPackage(Reservation):
    subReservation = create_relationship_to(['ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Reservation'], '子预定信息')


class EventReservation(Reservation):
    pass


class LodgingReservation(Reservation):
    checkinTime = create_relationship_to(['Date'], '入住时间')

    checkoutTime = create_relationship_to(['Date'], '退房时间')

    lodgingUnitDescription = create_relationship_to(['Text'], '旅馆房间描述')

    lodgingUnitType = create_relationship_to(['SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue', 'Text'], '旅馆房间房型')

    numAdults = create_relationship_to(['Integer', 'QuantitativeValue'], '大人人数')

    numChildren = create_relationship_to(['Integer', 'QuantitativeValue'], '小孩人数')


class FlightReservation(Reservation):
    boardingGroup = create_relationship_to(['Text'], '登机乘客分组')

    passengerPriorityStatus = create_relationship_to(['Text', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '乘客优先级状态')

    passengerSequenceNumber = create_relationship_to(['Text'], '乘客的顺序编号')

    securityScreening = create_relationship_to(['Text'], '安全检查')


class TrainReservation(Reservation):
    pass


class FoodEstablishmentReservation(Reservation):
    endTime = create_relationship_to(['Date'], '结束时刻')

    partySize = create_relationship_to(['Integer', 'QuantitativeValue'], '预约活动的参与人数')

    startTime = create_relationship_to(['Date'], '开始时刻')


class BusReservation(Reservation):
    pass


class RentalCarReservation(Reservation):
    dropoffLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '租车归还地点')

    dropoffTime = create_relationship_to(['Date'], '租车归还时间')

    pickupLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '接人地点')

    pickupTime = create_relationship_to(['Date'], '接人时间')


class Offer(Intangible):
    acceptedPaymentMethod = create_relationship_to(['PaymentCard', 'CreditCard', 'PaymentMethod', 'LoanOrCredit'], '卖家接受的支付方式')

    addOn = create_relationship_to(['AggregateOffer', 'Offer'], '附加品')

    advanceBookingRequirement = create_relationship_to(['QuantitativeValue'], '预定要求')

    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    areaServed = create_relationship_to(['City', 'Country', 'State', 'AdministrativeArea', 'Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '服务覆盖区域')

    availability = create_relationship_to(['ItemAvailability'], '供应状态')

    availabilityEnds = create_relationship_to(['Date'], '供应截止时间')

    availabilityStarts = create_relationship_to(['Date'], '供应开始时间')

    availableAtOrFrom = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place'], '报价地点')

    availableDeliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '支持的物流方式')

    businessFunction = create_relationship_to(['BusinessFunction'], '商业职能')

    category = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '类别')

    deliveryLeadTime = create_relationship_to(['QuantitativeValue'], '物流送货时间')

    eligibleCustomerType = create_relationship_to(['BusinessEntityType'], '适用的顾客类型')

    eligibleDuration = create_relationship_to(['QuantitativeValue'], '有效时间')

    eligibleQuantity = create_relationship_to(['QuantitativeValue'], '适用数量')

    eligibleRegion = create_relationship_to(['Text', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'GeoCircle', 'GeoShape'], '适用地区')

    eligibleTransactionVolume = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '适用购买数量')

    gtin12 = create_relationship_to(['Text'], '12位全球贸易品项识别码')

    gtin13 = create_relationship_to(['Text'], '13位全球贸易品项识别码')

    gtin14 = create_relationship_to(['Text'], '14位全球贸易品项识别码')

    gtin8 = create_relationship_to(['Text'], '8位全球贸易品项识别码')

    includesObject = create_relationship_to(['TypeAndQuantityNode'], '包含对象')

    ineligibleRegion = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text', 'GeoCircle', 'GeoShape'], '不适用地区')

    inventoryLevel = create_relationship_to(['QuantitativeValue'], '库存量')

    itemCondition = create_relationship_to(['OfferItemCondition'], '规格')

    itemOffered = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '销售物品')

    mpn = create_relationship_to(['Text'], '制造商零件编码')

    offeredBy = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '报价者')

    price = create_relationship_to(['Integer', 'Text'], '价格')

    priceCurrency = create_relationship_to(['Text'], '价格对应的货币单位')

    priceSpecification = create_relationship_to(['UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PriceSpecification'], '价格明细')

    priceValidUntil = create_relationship_to(['Date'], '价格有效截止日期')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    seller = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '卖家')

    serialNumber = create_relationship_to(['Text'], '序列号')

    sku = create_relationship_to(['Text'], '单品编号')

    validFrom = create_relationship_to(['Date'], '生效日期')

    validThrough = create_relationship_to(['Date'], '有效截止日期')

    warranty = create_relationship_to(['WarrantyPromise'], '担保')


class AggregateOffer(Offer):
    highPrice = create_relationship_to(['Text', 'Integer'], '最高价')

    lowPrice = create_relationship_to(['Text', 'Integer'], '最低价格')

    offerCount = create_relationship_to(['Integer'], '商品的报价总数')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')


class Event(Thing):
    about = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '关于')

    actor = create_relationship_to(['Person'], '演员')

    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    attendee = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '参与者')

    audience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '受众')

    composer = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '作曲者')

    contributor = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '贡献者')

    director = create_relationship_to(['Person'], '导演')

    doorTime = create_relationship_to(['Date'], '允许进场时间')

    duration = create_relationship_to(['Duration'], '持续时间')

    endDate = create_relationship_to(['Date'], '结束日期')

    eventStatus = create_relationship_to(['EventStatusType'], '活动的状态')

    funder = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '投资者')

    inLanguage = create_relationship_to(['Text', 'Language'], '使用语言')

    isAccessibleForFree = create_relationship_to(['Bool'], '是否免费')

    location = create_relationship_to(['PostalAddress', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text'], '地点')

    maximumAttendeeCapacity = create_relationship_to(['Integer'], '最多可容纳多少人参与')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')

    organizer = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '组织者')

    performer = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '表演者')

    previousStartDate = create_relationship_to(['Date'], '之前计划的开始日期')

    recordedIn = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '所属媒体记录')

    remainingAttendeeCapacity = create_relationship_to(['Integer'], '剩余可容纳的参与人数')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    sponsor = create_relationship_to(['Person', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '赞助者')

    startDate = create_relationship_to(['Date'], '开始日期')

    subEvent = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '子活动')

    superEvent = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '上一级的活动')

    translator = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '翻译者')

    typicalAgeRange = create_relationship_to(['Text'], '适应年龄段')

    workFeatured = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '特色作品')

    workPerformed = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '表演的作品')


class PublicationEvent(Event):
    isAccessibleForFree = create_relationship_to(['Bool'], '是否免费')

    publishedOn = create_relationship_to(['BroadcastService'], '发布的媒体')


class OnDemandEvent(PublicationEvent):
    pass


class BroadcastEvent(PublicationEvent):
    broadcastOfEvent = create_relationship_to(['ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Event'], '广播频道播出的活动')

    isLiveBroadcast = create_relationship_to(['Bool'], '是否直播')

    videoFormat = create_relationship_to(['Text'], '视频格式')


class EducationEvent(Event):
    pass


class DanceEvent(Event):
    pass


class SaleEvent(Event):
    pass


class FoodEvent(Event):
    pass


class BusinessEvent(Event):
    pass


class UserInteraction(Event):
    pass


class UserLikes(UserInteraction):
    pass


class UserPlays(UserInteraction):
    pass


class UserBlocks(UserInteraction):
    pass


class UserTweets(UserInteraction):
    pass


class UserPlusOnes(UserInteraction):
    pass


class UserPageVisits(UserInteraction):
    pass


class UserDownloads(UserInteraction):
    pass


class UserCheckins(UserInteraction):
    pass


class UserComments(UserInteraction):
    commentText = create_relationship_to(['Text'], '评论文字')

    commentTime = create_relationship_to(['Date'], '评论发表时间')

    creator = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Person'], '作者')

    discusses = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '讨论')

    replyToUrl = create_relationship_to(['Text'], '回复链接')


class ExhibitionEvent(Event):
    pass


class CourseInstance(Event):
    courseMode = create_relationship_to(['Text'], '课程的授课模式')

    instructor = create_relationship_to(['Person'], '教师')


class ComedyEvent(Event):
    pass


class ScreeningEvent(Event):
    subtitleLanguage = create_relationship_to(['Text', 'Language'], '字幕语言')

    videoFormat = create_relationship_to(['Text'], '视频格式')

    workPresented = create_relationship_to(['Movie'], '上映的作品')


class MusicEvent(Event):
    pass


class VisualArtsEvent(Event):
    pass


class DeliveryEvent(Event):
    accessCode = create_relationship_to(['Text'], '存取码')

    availableFrom = create_relationship_to(['Date'], '提货开始时间')

    availableThrough = create_relationship_to(['Date'], '提货截止时间')

    hasDeliveryMethod = create_relationship_to(['LockerDelivery', 'ParcelService', 'DeliveryMethod'], '物流送货方式')


class ChildrensEvent(Event):
    pass


class Festival(Event):
    pass


class LiteraryEvent(Event):
    pass


class SocialEvent(Event):
    pass


class TheaterEvent(Event):
    pass


class SportsEvent(Event):
    awayTeam = create_relationship_to(['Person', 'SportsTeam'], '客场队')

    competitor = create_relationship_to(['SportsTeam', 'Person'], '竞技对手')

    homeTeam = create_relationship_to(['Person', 'SportsTeam'], '主队')


class Product(Thing):
    additionalProperty = create_relationship_to(['LocationFeatureSpecification', 'PropertyValue'], '附加属性')

    aggregateRating = create_relationship_to(['AggregateRating'], '总体评分')

    audience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '受众')

    award = create_relationship_to(['Text'], '所获奖项')

    brand = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization', 'Brand'], '品牌')

    category = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '类别')

    color = create_relationship_to(['Text'], '颜色')

    depth = create_relationship_to(['QuantitativeValue', 'Distance'], '深度')

    gtin12 = create_relationship_to(['Text'], '12位全球贸易品项识别码')

    gtin13 = create_relationship_to(['Text'], '13位全球贸易品项识别码')

    gtin14 = create_relationship_to(['Text'], '14位全球贸易品项识别码')

    gtin8 = create_relationship_to(['Text'], '8位全球贸易品项识别码')

    height = create_relationship_to(['Distance', 'QuantitativeValue'], '高度')

    isAccessoryOrSparePartFor = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '是另一产品的附件或备件')

    isConsumableFor = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '下游产品')

    isRelatedTo = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service'], '相关')

    isSimilarTo = create_relationship_to(['Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'Service', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product'], '相似')

    itemCondition = create_relationship_to(['OfferItemCondition'], '规格')

    logo = create_relationship_to(['Text', 'Barcode', 'ImageObject'], '商标')

    manufacturer = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制造商')

    material = create_relationship_to(['ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Product', 'Text'], '材质')

    model = create_relationship_to(['Text', 'ProductModel'], '型号')

    mpn = create_relationship_to(['Text'], '制造商零件编码')

    offers = create_relationship_to(['AggregateOffer', 'Offer'], '报价')

    productID = create_relationship_to(['Text'], '产品ID')

    productionDate = create_relationship_to(['Date'], '生产日期')

    purchaseDate = create_relationship_to(['Date'], '购买日期')

    releaseDate = create_relationship_to(['Date'], '发布日期')

    review = create_relationship_to(['ClaimReview', 'Review'], '事物的评论')

    sku = create_relationship_to(['Text'], '单品编号')

    weight = create_relationship_to(['QuantitativeValue'], '重量')

    width = create_relationship_to(['Distance', 'QuantitativeValue'], '宽度')


class Vehicle(Product):
    cargoVolume = create_relationship_to(['QuantitativeValue'], '汽车载货容量')

    dateVehicleFirstRegistered = create_relationship_to(['Date'], '汽车首次注册日期')

    driveWheelConfiguration = create_relationship_to(['DriveWheelConfigurationValue', 'Text'], '驱动轮配置')

    fuelConsumption = create_relationship_to(['QuantitativeValue'], '耗油率')

    fuelEfficiency = create_relationship_to(['QuantitativeValue'], '油耗值')

    fuelType = create_relationship_to(['Text', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '燃料类型')

    knownVehicleDamages = create_relationship_to(['Text'], '已知汽车故障')

    mileageFromOdometer = create_relationship_to(['QuantitativeValue'], '里程数')

    numberOfAirbags = create_relationship_to(['Integer', 'Text'], '汽车安全气囊总数')

    numberOfAxles = create_relationship_to(['Integer', 'QuantitativeValue'], '汽车轮轴数')

    numberOfDoors = create_relationship_to(['QuantitativeValue', 'Integer'], '汽车车门数')

    numberOfForwardGears = create_relationship_to(['Integer', 'QuantitativeValue'], '前进档位数')

    numberOfPreviousOwners = create_relationship_to(['QuantitativeValue', 'Integer'], '历任车主数')

    productionDate = create_relationship_to(['Date'], '生产日期')

    purchaseDate = create_relationship_to(['Date'], '购买日期')

    steeringPosition = create_relationship_to(['SteeringPositionValue'], '方向盘位置')

    vehicleConfiguration = create_relationship_to(['Text'], '车辆配置')

    vehicleEngine = create_relationship_to(['EngineSpecification'], '车辆引擎')

    vehicleIdentificationNumber = create_relationship_to(['Text'], '车辆识别号码')

    vehicleInteriorColor = create_relationship_to(['Text'], '车辆内饰颜色')

    vehicleInteriorType = create_relationship_to(['Text'], '车辆内饰类型')

    vehicleModelDate = create_relationship_to(['Date'], '车辆型号发布日期')

    vehicleSeatingCapacity = create_relationship_to(['QuantitativeValue', 'Integer'], '车辆可容纳最大人数')

    vehicleSpecialUsage = create_relationship_to(['Text'], '车辆特殊用途')

    vehicleTransmission = create_relationship_to(['Text', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'QualitativeValue'], '车辆传动装置')


class Car(Vehicle):
    pass


class SomeProducts(Product):
    inventoryLevel = create_relationship_to(['QuantitativeValue'], '库存量')


class IndividualProduct(Product):
    serialNumber = create_relationship_to(['Text'], '序列号')


class ProductModel(Product):
    isVariantOf = create_relationship_to(['ProductModel'], '变形')

    predecessorOf = create_relationship_to(['ProductModel'], '上一代型号')

    successorOf = create_relationship_to(['ProductModel'], '上一代型号')


class HowToSection(ListItem,CreativeWork,ItemList):
    pass


class VideoGame(SoftwareApplication,Game):
    actor = create_relationship_to(['Person'], '演员')

    cheatCode = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '游戏作弊码')

    director = create_relationship_to(['Person'], '导演')

    gamePlatform = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '游戏平台')

    gameServer = create_relationship_to(['GameServer'], '游戏服务器')

    gameTip = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '游戏攻略')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    playMode = create_relationship_to(['GamePlayMode'], '游戏玩家模式')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class TVSeason(CreativeWorkSeason,CreativeWork):
    countryOfOrigin = create_relationship_to(['Country'], '影片制作国家')


class HowToTip(ListItem,CreativeWork):
    pass


class HowToStep(ListItem,CreativeWork,ItemList):
    pass


class CreativeWorkSeries(Series,CreativeWork):
    endDate = create_relationship_to(['Date'], '结束日期')

    issn = create_relationship_to(['Text'], 'ISSN号')

    startDate = create_relationship_to(['Date'], '开始日期')


class BookSeries(CreativeWorkSeries):
    pass


class RadioSeries(CreativeWorkSeries):
    actor = create_relationship_to(['Person'], '演员')

    containsSeason = create_relationship_to(['RadioSeason', 'TVSeason', 'CreativeWorkSeason'], '包含哪些季')

    director = create_relationship_to(['Person'], '导演')

    episode = create_relationship_to(['RadioEpisode', 'TVEpisode', 'Episode'], '剧集')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    numberOfEpisodes = create_relationship_to(['Integer'], '剧集数')

    numberOfSeasons = create_relationship_to(['Integer'], '季数')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class Periodical(CreativeWorkSeries):
    pass


class MovieSeries(CreativeWorkSeries):
    actor = create_relationship_to(['Person'], '演员')

    director = create_relationship_to(['Person'], '导演')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class VideoGameSeries(CreativeWorkSeries):
    actor = create_relationship_to(['Person'], '演员')

    characterAttribute = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '人物角色属性')

    cheatCode = create_relationship_to(['CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'CreativeWork'], '游戏作弊码')

    containsSeason = create_relationship_to(['RadioSeason', 'TVSeason', 'CreativeWorkSeason'], '包含哪些季')

    director = create_relationship_to(['Person'], '导演')

    episode = create_relationship_to(['RadioEpisode', 'TVEpisode', 'Episode'], '剧集')

    gameItem = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '游戏道具')

    gameLocation = create_relationship_to(['Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'StadiumOrArena', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Campground', 'Cemetery', 'FireStation', 'Hospital', 'MovieTheater', 'PoliceStation', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'Place', 'Text', 'PostalAddress'], '游戏地址')

    gamePlatform = create_relationship_to(['Text', 'Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '游戏平台')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    numberOfEpisodes = create_relationship_to(['Integer'], '剧集数')

    numberOfPlayers = create_relationship_to(['QuantitativeValue'], '玩家数')

    numberOfSeasons = create_relationship_to(['Integer'], '季数')

    playMode = create_relationship_to(['GamePlayMode'], '游戏玩家模式')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    quest = create_relationship_to(['Action', 'AssessAction', 'ChooseAction', 'VoteAction', 'IgnoreAction', 'ReactAction', 'WantAction', 'AgreeAction', 'DisagreeAction', 'DislikeAction', 'EndorseAction', 'LikeAction', 'ReviewAction', 'ConsumeAction', 'DrinkAction', 'EatAction', 'InstallAction', 'ListenAction', 'ReadAction', 'UseAction', 'WearAction', 'ViewAction', 'WatchAction', 'ControlAction', 'DeactivateAction', 'ResumeAction', 'SuspendAction', 'ActivateAction', 'CreateAction', 'DrawAction', 'FilmAction', 'PaintAction', 'PhotographAction', 'WriteAction', 'CookAction', 'FindAction', 'TrackAction', 'CheckAction', 'DiscoverAction', 'InteractAction', 'JoinAction', 'LeaveAction', 'MarryAction', 'RegisterAction', 'SubscribeAction', 'UnRegisterAction', 'BefriendAction', 'CommunicateAction', 'InformAction', 'RsvpAction', 'ConfirmAction', 'InviteAction', 'ReplyAction', 'ShareAction', 'AskAction', 'CheckInAction', 'CheckOutAction', 'CommentAction', 'FollowAction', 'MoveAction', 'TravelAction', 'ArriveAction', 'DepartAction', 'OrganizeAction', 'PlanAction', 'ReserveAction', 'ScheduleAction', 'CancelAction', 'AllocateAction', 'AssignAction', 'AuthorizeAction', 'RejectAction', 'AcceptAction', 'ApplyAction', 'BookmarkAction', 'PlayAction', 'ExerciseAction', 'PerformAction', 'SearchAction', 'TradeAction', 'BuyAction', 'DonateAction', 'OrderAction', 'PayAction', 'QuoteAction', 'RentAction', 'SellAction', 'TipAction', 'TransferAction', 'BorrowAction', 'DownloadAction', 'GiveAction', 'LendAction', 'ReceiveAction', 'ReturnAction', 'SendAction', 'TakeAction', 'UpdateAction', 'AddAction', 'InsertAction', 'PrependAction', 'AppendAction', 'DeleteAction', 'ReplaceAction', 'AchieveAction', 'LoseAction', 'TieAction', 'WinAction', 'CreativeWork', 'CreativeWorkSeason', 'RadioSeason', 'TVSeason', 'DataCatalog', 'Dataset', 'DataFeed', 'DigitalDocument', 'NoteDigitalDocument', 'PresentationDigitalDocument', 'SpreadsheetDigitalDocument', 'TextDigitalDocument', 'Episode', 'RadioEpisode', 'TVEpisode', 'Game', 'VideoGame', 'HowTo', 'Recipe', 'Map', 'MediaObject', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'Menu', 'MenuSection', 'Message', 'EmailMessage', 'Movie', 'MusicComposition', 'MusicPlaylist', 'MusicRelease', 'MusicAlbum', 'MusicRecording', 'Painting', 'Photograph', 'PublicationIssue', 'PublicationVolume', 'Question', 'Review', 'ClaimReview', 'Sculpture', 'Season', 'SoftwareApplication', 'WebApplication', 'MobileApplication', 'SoftwareSourceCode', 'VisualArtwork', 'WebPage', 'AboutPage', 'CheckoutPage', 'CollectionPage', 'ImageGallery', 'VideoGallery', 'ContactPage', 'ItemPage', 'ProfilePage', 'QAPage', 'SearchResultsPage', 'WebPageElement', 'WPAdBlock', 'WPFooter', 'WPHeader', 'WPSideBar', 'SiteNavigationElement', 'Table', 'WebSite', 'Article', 'NewsArticle', 'Report', 'ScholarlyArticle', 'SocialMediaPosting', 'BlogPosting', 'LiveBlogPosting', 'DiscussionForumPosting', 'TechArticle', 'APIReference', 'Blog', 'Book', 'Clip', 'MovieClip', 'RadioClip', 'TVClip', 'VideoGameClip', 'Code', 'Comment', 'Answer', 'Conversation', 'Course', 'CreativeWorkSeries', 'MovieSeries', 'Periodical', 'RadioSeries', 'TVSeries', 'VideoGameSeries', 'BookSeries', 'HowToDirection', 'HowToSection', 'HowToStep', 'HowToTip', 'Event', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'BroadcastEvent', 'OnDemandEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'UserInteraction', 'UserLikes', 'UserPageVisits', 'UserPlays', 'UserPlusOnes', 'UserTweets', 'UserBlocks', 'UserCheckins', 'UserComments', 'UserDownloads', 'VisualArtsEvent', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'Intangible', 'Invoice', 'ItemList', 'OfferCatalog', 'BreadcrumbList', 'JobPosting', 'Language', 'ListItem', 'HowToItem', 'HowToSupply', 'HowToTool', 'MenuItem', 'Offer', 'AggregateOffer', 'Order', 'OrderItem', 'ParcelDelivery', 'Permit', 'GovernmentPermit', 'ProgramMembership', 'PropertyValueSpecification', 'Quantity', 'Distance', 'Duration', 'Energy', 'Mass', 'Rating', 'AggregateRating', 'Reservation', 'ReservationPackage', 'TaxiReservation', 'TrainReservation', 'BusReservation', 'EventReservation', 'FlightReservation', 'FoodEstablishmentReservation', 'LodgingReservation', 'RentalCarReservation', 'Role', 'OrganizationRole', 'EmployeeRole', 'PerformanceRole', 'Seat', 'Series', 'Service', 'Taxi', 'TaxiService', 'BroadcastService', 'CableOrSatelliteService', 'FinancialProduct', 'InvestmentOrDeposit', 'DepositAccount', 'LoanOrCredit', 'CreditCard', 'PaymentService', 'BankAccount', 'CurrencyConversionService', 'PaymentCard', 'FoodService', 'GovernmentService', 'ServiceChannel', 'StructuredValue', 'TypeAndQuantityNode', 'WarrantyPromise', 'ContactPoint', 'PostalAddress', 'DatedMoneySpecification', 'EngineSpecification', 'GeoCoordinates', 'GeoShape', 'GeoCircle', 'InteractionCounter', 'MonetaryAmount', 'NutritionInformation', 'OpeningHoursSpecification', 'OwnershipInfo', 'PriceSpecification', 'UnitPriceSpecification', 'CompoundPriceSpecification', 'DeliveryChargeSpecification', 'PaymentChargeSpecification', 'PropertyValue', 'LocationFeatureSpecification', 'QuantitativeValue', 'Ticket', 'Trip', 'BusTrip', 'Flight', 'TrainTrip', 'AlignmentObject', 'Audience', 'BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'BedDetails', 'Brand', 'BroadcastChannel', 'RadioChannel', 'TelevisionChannel', 'ComputerLanguage', 'DataFeedItem', 'Demand', 'DigitalDocumentPermission', 'EntryPoint', 'Enumeration', 'EventStatusType', 'GamePlayMode', 'GameServerStatus', 'GenderType', 'ItemAvailability', 'ItemListOrderType', 'MapCategoryType', 'MusicAlbumProductionType', 'MusicAlbumReleaseType', 'MusicReleaseFormatType', 'OfferItemCondition', 'OrderStatus', 'PaymentMethod', 'PaymentStatusType', 'QualitativeValue', 'SteeringPositionValue', 'DriveWheelConfigurationValue', 'ReservationStatusType', 'RestrictedDiet', 'RsvpResponseType', 'Specialty', 'WarrantyScope', 'ActionStatusType', 'BoardingPolicyType', 'BookFormatType', 'BusinessEntityType', 'BusinessFunction', 'ContactPointOption', 'DayOfWeek', 'DeliveryMethod', 'LockerDelivery', 'ParcelService', 'DigitalDocumentPermissionType', 'GameServer', 'Organization', 'PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Person', 'Place', 'Residence', 'ApartmentComplex', 'GatedResidenceCommunity', 'TouristAttraction', 'Accommodation', 'Apartment', 'CampingPitch', 'House', 'SingleFamilyResidence', 'Room', 'HotelRoom', 'MeetingRoom', 'Suite', 'AdministrativeArea', 'City', 'Country', 'State', 'CivicStructure', 'Crematorium', 'EventVenue', 'GovernmentBuilding', 'LegislativeBuilding', 'CityHall', 'Courthouse', 'DefenceEstablishment', 'Embassy', 'Museum', 'MusicVenue', 'Park', 'ParkingFacility', 'PerformingArtsTheater', 'PlaceOfWorship', 'Synagogue', 'BuddhistTemple', 'CatholicChurch', 'Church', 'HinduTemple', 'Mosque', 'Playground', 'RVPark', 'SubwayStation', 'TaxiStand', 'TrainStation', 'Zoo', 'Airport', 'Aquarium', 'Beach', 'Bridge', 'BusStation', 'BusStop', 'Cemetery', 'Landform', 'Mountain', 'Volcano', 'BodyOfWater', 'Canal', 'LakeBodyOfWater', 'OceanBodyOfWater', 'Pond', 'Reservoir', 'RiverBodyOfWater', 'SeaBodyOfWater', 'Waterfall', 'Continent', 'LandmarksOrHistoricalBuildings', 'Product', 'ProductModel', 'SomeProducts', 'Vehicle', 'Car', 'IndividualProduct', 'Thing'], '游戏任务')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class TVSeries(CreativeWorkSeries,CreativeWork):
    actor = create_relationship_to(['Person'], '演员')

    containsSeason = create_relationship_to(['RadioSeason', 'TVSeason', 'CreativeWorkSeason'], '包含哪些季')

    countryOfOrigin = create_relationship_to(['Country'], '影片制作国家')

    director = create_relationship_to(['Person'], '导演')

    episode = create_relationship_to(['RadioEpisode', 'TVEpisode', 'Episode'], '剧集')

    musicBy = create_relationship_to(['Person', 'MusicGroup'], '作曲者')

    numberOfEpisodes = create_relationship_to(['Integer'], '剧集数')

    numberOfSeasons = create_relationship_to(['Integer'], '季数')

    productionCompany = create_relationship_to(['PerformingGroup', 'TheaterGroup', 'DanceGroup', 'MusicGroup', 'SportsOrganization', 'SportsTeam', 'Airline', 'Corporation', 'EducationalOrganization', 'ElementarySchool', 'HighSchool', 'MiddleSchool', 'Preschool', 'School', 'CollegeOrUniversity', 'GovernmentOrganization', 'LocalBusiness', 'LodgingBusiness', 'Motel', 'Resort', 'BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'ProfessionalService', 'RadioStation', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'SportsClub', 'StadiumOrArena', 'TennisComplex', 'BowlingAlley', 'ExerciseGym', 'GolfCourse', 'HealthClub', 'PublicSwimmingPool', 'SkiResort', 'Store', 'TireShop', 'ToyStore', 'WholesaleStore', 'AutoPartsStore', 'BikeStore', 'BookStore', 'ClothingStore', 'ComputerStore', 'ConvenienceStore', 'DepartmentStore', 'ElectronicsStore', 'Florist', 'FurnitureStore', 'GardenStore', 'GroceryStore', 'HardwareStore', 'HobbyShop', 'HomeGoodsStore', 'JewelryStore', 'LiquorStore', 'MensClothingStore', 'MobilePhoneStore', 'MovieRentalStore', 'MusicStore', 'OfficeEquipmentStore', 'OutletStore', 'PawnShop', 'PetStore', 'ShoeStore', 'SportingGoodsStore', 'TelevisionStation', 'TouristInformationCenter', 'TravelAgency', 'AnimalShelter', 'AutomotiveBusiness', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'AutoBodyShop', 'AutoDealer', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'FireStation', 'Hospital', 'PoliceStation', 'EmploymentAgency', 'EntertainmentBusiness', 'MovieTheater', 'NightClub', 'AdultEntertainment', 'AmusementPark', 'ArtGallery', 'Casino', 'ComedyClub', 'FinancialService', 'InsuranceAgency', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'FoodEstablishment', 'IceCreamShop', 'Restaurant', 'Winery', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'FastFoodRestaurant', 'GovernmentOffice', 'PostOffice', 'HealthAndBeautyBusiness', 'NailSalon', 'TattooParlor', 'BeautySalon', 'DaySpa', 'HairSalon', 'HomeAndConstructionBusiness', 'HousePainter', 'HVACBusiness', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'Electrician', 'GeneralContractor', 'InternetCafe', 'LegalService', 'Notary', 'Attorney', 'Library', 'MedicalOrganization', 'Pharmacy', 'Physician', 'NGO', 'Organization'], '制作公司')

    trailer = create_relationship_to(['VideoObject'], '预告片')


class HowToDirection(ListItem,CreativeWork):
    afterMedia = create_relationship_to(['MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'MediaObject', 'Text'], '操作前的媒体展示')

    beforeMedia = create_relationship_to(['Text', 'MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'MediaObject'], '操作后的媒体展示')

    duringMedia = create_relationship_to(['MusicVideoObject', 'VideoObject', 'AudioObject', 'DataDownload', 'ImageObject', 'Barcode', 'MediaObject', 'Text'], '操作中的媒体展示')

    performTime = create_relationship_to(['Duration'], '执行时间')

    prepTime = create_relationship_to(['Duration'], '准备时间')

    supply = create_relationship_to(['Text', 'HowToSupply'], '相关物料')

    tool = create_relationship_to(['HowToTool', 'Text'], '相关工具')

    totalTime = create_relationship_to(['Duration'], '总时间')


class LocalBusiness(Organization,Place):
    currenciesAccepted = create_relationship_to(['Text'], '接收的货币')

    openingHours = create_relationship_to(['Text'], '开放时间')

    paymentAccepted = create_relationship_to(['Text'], '接受的支付方式')

    priceRange = create_relationship_to(['Text'], '价格范围')


class AnimalShelter(LocalBusiness):
    pass


class FoodEstablishment(LocalBusiness):
    acceptsReservations = create_relationship_to(['Text', 'Bool'], '是否接受预定')

    hasMenu = create_relationship_to(['Text', 'Menu'], '目录')

    servesCuisine = create_relationship_to(['Text'], '主营菜系')

    starRating = create_relationship_to(['AggregateRating', 'Rating'], '星级评分')


class CafeOrCoffeeShop(FoodEstablishment):
    pass


class Bakery(FoodEstablishment):
    pass


class IceCreamShop(FoodEstablishment):
    pass


class Restaurant(FoodEstablishment):
    pass


class FastFoodRestaurant(FoodEstablishment):
    pass


class Winery(FoodEstablishment):
    pass


class BarOrPub(FoodEstablishment):
    pass


class Brewery(FoodEstablishment):
    pass


class LegalService(LocalBusiness):
    pass


class Attorney(LegalService):
    pass


class Notary(LegalService):
    pass


class HomeAndConstructionBusiness(LocalBusiness):
    pass


class HousePainter(HomeAndConstructionBusiness):
    pass


class GeneralContractor(HomeAndConstructionBusiness):
    pass


class Electrician(HomeAndConstructionBusiness):
    pass


class MovingCompany(HomeAndConstructionBusiness):
    pass


class HVACBusiness(HomeAndConstructionBusiness):
    pass


class Locksmith(HomeAndConstructionBusiness):
    pass


class Plumber(HomeAndConstructionBusiness):
    pass


class RoofingContractor(HomeAndConstructionBusiness):
    pass


class RealEstateAgent(LocalBusiness):
    pass


class ChildCare(LocalBusiness):
    pass


class InternetCafe(LocalBusiness):
    pass


class RadioStation(LocalBusiness):
    pass


class GovernmentOffice(LocalBusiness):
    pass


class PostOffice(GovernmentOffice):
    pass


class Library(LocalBusiness):
    pass


class TouristInformationCenter(LocalBusiness):
    pass


class ProfessionalService(LocalBusiness):
    pass


class SelfStorage(LocalBusiness):
    pass


class EntertainmentBusiness(LocalBusiness):
    pass


class AmusementPark(EntertainmentBusiness):
    pass


class Casino(EntertainmentBusiness):
    pass


class MovieTheater(CivicStructure,EntertainmentBusiness):
    screenCount = create_relationship_to(['Integer'], '放映厅数量')


class NightClub(EntertainmentBusiness):
    pass


class ComedyClub(EntertainmentBusiness):
    pass


class AdultEntertainment(EntertainmentBusiness):
    pass


class ArtGallery(EntertainmentBusiness):
    pass


class ShoppingCenter(LocalBusiness):
    pass


class TelevisionStation(LocalBusiness):
    pass


class DryCleaningOrLaundry(LocalBusiness):
    pass


class EmploymentAgency(LocalBusiness):
    pass


class EmergencyService(LocalBusiness):
    pass


class PoliceStation(CivicStructure,EmergencyService):
    pass


class FireStation(CivicStructure,EmergencyService):
    pass


class Hospital(CivicStructure,MedicalOrganization,EmergencyService):
    pass


class FinancialService(LocalBusiness):
    feesAndCommissionsSpecification = create_relationship_to(['Text'], '费用和佣金详情')


class InsuranceAgency(FinancialService):
    pass


class BankOrCreditUnion(FinancialService):
    pass


class AutomatedTeller(FinancialService):
    pass


class AccountingService(FinancialService):
    pass


class HealthAndBeautyBusiness(LocalBusiness):
    pass


class NailSalon(HealthAndBeautyBusiness):
    pass


class HairSalon(HealthAndBeautyBusiness):
    pass


class DaySpa(HealthAndBeautyBusiness):
    pass


class TattooParlor(HealthAndBeautyBusiness):
    pass


class BeautySalon(HealthAndBeautyBusiness):
    pass


class TravelAgency(LocalBusiness):
    pass


class SportsActivityLocation(LocalBusiness):
    pass


class ExerciseGym(SportsActivityLocation):
    pass


class GolfCourse(SportsActivityLocation):
    pass


class SportsClub(SportsActivityLocation):
    pass


class StadiumOrArena(CivicStructure,SportsActivityLocation):
    pass


class TennisComplex(SportsActivityLocation):
    pass


class SkiResort(SportsActivityLocation):
    pass


class PublicSwimmingPool(SportsActivityLocation):
    pass


class BowlingAlley(SportsActivityLocation):
    pass


class Dentist(MedicalOrganization,LocalBusiness):
    pass


class Store(LocalBusiness):
    pass


class GroceryStore(Store):
    pass


class JewelryStore(Store):
    pass


class HomeGoodsStore(Store):
    pass


class TireShop(Store):
    pass


class MovieRentalStore(Store):
    pass


class ToyStore(Store):
    pass


class BookStore(Store):
    pass


class OutletStore(Store):
    pass


class MobilePhoneStore(Store):
    pass


class LiquorStore(Store):
    pass


class BikeStore(Store):
    pass


class SportingGoodsStore(Store):
    pass


class OfficeEquipmentStore(Store):
    pass


class MusicStore(Store):
    pass


class ComputerStore(Store):
    pass


class ShoeStore(Store):
    pass


class PetStore(Store):
    pass


class Florist(Store):
    pass


class PawnShop(Store):
    pass


class ConvenienceStore(Store):
    pass


class ElectronicsStore(Store):
    pass


class GardenStore(Store):
    pass


class FurnitureStore(Store):
    pass


class HardwareStore(Store):
    pass


class HobbyShop(Store):
    pass


class WholesaleStore(Store):
    pass


class DepartmentStore(Store):
    pass


class MensClothingStore(Store):
    pass


class ClothingStore(Store):
    pass


class LodgingBusiness(LocalBusiness):
    amenityFeature = create_relationship_to(['LocationFeatureSpecification'], '特色服务')

    audience = create_relationship_to(['BusinessAudience', 'EducationalAudience', 'PeopleAudience', 'ParentAudience', 'Audience'], '受众')

    availableLanguage = create_relationship_to(['Language', 'Text'], '支持的语言')

    checkinTime = create_relationship_to(['Date'], '入住时间')

    checkoutTime = create_relationship_to(['Date'], '退房时间')

    petsAllowed = create_relationship_to(['Text', 'Bool'], '是否允许带宠物')

    starRating = create_relationship_to(['AggregateRating', 'Rating'], '星级评分')


class BedAndBreakfast(LodgingBusiness):
    pass


class Motel(LodgingBusiness):
    pass


class Hotel(LodgingBusiness):
    pass


class Hostel(LodgingBusiness):
    pass


class Resort(LodgingBusiness):
    pass


class Campground(CivicStructure,LodgingBusiness):
    pass


class RecyclingCenter(LocalBusiness):
    pass


class AutomotiveBusiness(LocalBusiness):
    pass


class AutoRepair(AutomotiveBusiness):
    pass


class MotorcycleDealer(AutomotiveBusiness):
    pass


class AutoRental(AutomotiveBusiness):
    pass


class AutoDealer(AutomotiveBusiness):
    pass


class GasStation(AutomotiveBusiness):
    pass


class AutoBodyShop(AutomotiveBusiness):
    pass


class MotorcycleRepair(AutomotiveBusiness):
    pass


class AutoWash(AutomotiveBusiness):
    pass


class PaymentCard(PaymentMethod,FinancialProduct):
    pass


class CreditCard(LoanOrCredit,PaymentCard):
    pass


class DepositAccount(BankAccount,InvestmentOrDeposit):
    pass


class HealthClub(HealthAndBeautyBusiness,SportsActivityLocation):
    pass


class AutoPartsStore(Store,AutomotiveBusiness):
    pass



class Text(Thing):
    pass
  
  
class Date(Thing):
    pass
    
    
class Bool(Thing):
    pass
    

class Integer(Thing):
    pass


class Float(Thing):
    pass  
