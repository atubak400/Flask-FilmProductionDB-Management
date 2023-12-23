-- Create ProductionCompany table
CREATE TABLE ProductionCompany (
    CompanyName VARCHAR(100) PRIMARY KEY,
    Address TEXT NOT NULL,
    ZIPCode VARCHAR(20) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Nation VARCHAR(50) NOT NULL,
    TypeOfOrganization VARCHAR(50) NOT NULL,
    NumEmployees INT NOT NULL,
    NetValue DECIMAL(10, 2) NOT NULL,
    RegistrationDate DATE NOT NULL,
    RegistrationOffice VARCHAR(100) NOT NULL,
    RegistrationFee DECIMAL(10, 2) NOT NULL
);

-- Create Employee table
CREATE TABLE Employee (
    EmployeeID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    MiddleName VARCHAR(50),
    DateOfBirth DATE NOT NULL,
    CommencementDate DATE NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL,
    CompanyName VARCHAR(100) NOT NULL,
    FOREIGN KEY (CompanyName) REFERENCES ProductionCompany(CompanyName)
);

-- Create Film table
CREATE TABLE Film (
    MovieCode VARCHAR(50) PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    FirstReleaseYear INT NOT NULL
);

-- Create Grant table
CREATE TABLE "Grant" (
    GrantTitle VARCHAR(100) PRIMARY KEY,
    FundingOrganization VARCHAR(100) NOT NULL,
    MaxMonetaryValue DECIMAL(10, 2) NOT NULL,
    DeadlineForSubmission DATE NOT NULL
);

-- Create Crew table
CREATE TABLE Crew (
    CrewID SERIAL PRIMARY KEY,
    Role VARCHAR(50) NOT NULL,
    RoleDescription TEXT,
    Bonus DECIMAL(10, 2) NOT NULL,
    EmployeeID INT NOT NULL,
    MovieCode VARCHAR(50) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (MovieCode) REFERENCES Film(MovieCode)
);

-- Create GrantApplication table
CREATE TABLE GrantApplication (
    ApplicationID SERIAL PRIMARY KEY,
    ApplicationDate DATE NOT NULL,
    DesiredAmount DECIMAL(10, 2) NOT NULL,
    Outcome VARCHAR(50) NOT NULL,
    GrantTitle VARCHAR(100) NOT NULL,
    CompanyName VARCHAR(100) NOT NULL,
    FOREIGN KEY (GrantTitle) REFERENCES "Grant"(GrantTitle),
    FOREIGN KEY (CompanyName) REFERENCES ProductionCompany(CompanyName)
);

-- Create ContactInformation table
CREATE TABLE ContactInformation (
    ContactID SERIAL PRIMARY KEY,
    TelephoneNumber VARCHAR(20) NOT NULL,
    TelephoneNumberDescription VARCHAR(50) NOT NULL,
    NationalInsuranceNumber VARCHAR(20) NOT NULL,
    PassportNumber VARCHAR(20) NOT NULL,
    EmployeeID INT NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
