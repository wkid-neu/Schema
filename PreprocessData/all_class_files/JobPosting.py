from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class JobPosting(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, baseSalary=None, datePosted=None, educationRequirements=None, employmentType=None, experienceRequirements=None, hiringOrganization=None, incentiveCompensation=None, industry=None, jobBenefits=None, jobLocation=None, occupationalCategory=None, qualifications=None, responsibilities=None, salaryCurrency=None, skills=None, specialCommitments=None, title=None, validThrough=None, workHours=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.baseSalary = baseSalary
        self.datePosted = datePosted
        self.educationRequirements = educationRequirements
        self.employmentType = employmentType
        self.experienceRequirements = experienceRequirements
        self.hiringOrganization = hiringOrganization
        self.incentiveCompensation = incentiveCompensation
        self.industry = industry
        self.jobBenefits = jobBenefits
        self.jobLocation = jobLocation
        self.occupationalCategory = occupationalCategory
        self.qualifications = qualifications
        self.responsibilities = responsibilities
        self.salaryCurrency = salaryCurrency
        self.skills = skills
        self.specialCommitments = specialCommitments
        self.title = title
        self.validThrough = validThrough
        self.workHours = workHours

    def set_baseSalary(self, baseSalary):
        self.baseSalary = baseSalary

    def get_baseSalary(self):
        return self.baseSalary

    def set_datePosted(self, datePosted):
        self.datePosted = datePosted

    def get_datePosted(self):
        return self.datePosted

    def set_educationRequirements(self, educationRequirements):
        self.educationRequirements = educationRequirements

    def get_educationRequirements(self):
        return self.educationRequirements

    def set_employmentType(self, employmentType):
        self.employmentType = employmentType

    def get_employmentType(self):
        return self.employmentType

    def set_experienceRequirements(self, experienceRequirements):
        self.experienceRequirements = experienceRequirements

    def get_experienceRequirements(self):
        return self.experienceRequirements

    def set_hiringOrganization(self, hiringOrganization):
        self.hiringOrganization = hiringOrganization

    def get_hiringOrganization(self):
        return self.hiringOrganization

    def set_incentiveCompensation(self, incentiveCompensation):
        self.incentiveCompensation = incentiveCompensation

    def get_incentiveCompensation(self):
        return self.incentiveCompensation

    def set_industry(self, industry):
        self.industry = industry

    def get_industry(self):
        return self.industry

    def set_jobBenefits(self, jobBenefits):
        self.jobBenefits = jobBenefits

    def get_jobBenefits(self):
        return self.jobBenefits

    def set_jobLocation(self, jobLocation):
        self.jobLocation = jobLocation

    def get_jobLocation(self):
        return self.jobLocation

    def set_occupationalCategory(self, occupationalCategory):
        self.occupationalCategory = occupationalCategory

    def get_occupationalCategory(self):
        return self.occupationalCategory

    def set_qualifications(self, qualifications):
        self.qualifications = qualifications

    def get_qualifications(self):
        return self.qualifications

    def set_responsibilities(self, responsibilities):
        self.responsibilities = responsibilities

    def get_responsibilities(self):
        return self.responsibilities

    def set_salaryCurrency(self, salaryCurrency):
        self.salaryCurrency = salaryCurrency

    def get_salaryCurrency(self):
        return self.salaryCurrency

    def set_skills(self, skills):
        self.skills = skills

    def get_skills(self):
        return self.skills

    def set_specialCommitments(self, specialCommitments):
        self.specialCommitments = specialCommitments

    def get_specialCommitments(self):
        return self.specialCommitments

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_validThrough(self, validThrough):
        self.validThrough = validThrough

    def get_validThrough(self):
        return self.validThrough

    def set_workHours(self, workHours):
        self.workHours = workHours

    def get_workHours(self):
        return self.workHours


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
