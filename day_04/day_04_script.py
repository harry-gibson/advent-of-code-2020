import re

class PassportValidator():
    
    REQUIRED_FIELDS = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    
    def __init__(self):
        self.datafields = {}
        
    def IsValid(self):
        return all([f in self.datafields.keys() for f in PassportValidator.REQUIRED_FIELDS])
    
    def AddBatchRow(self, row):
        items = row.split()
        for item in items:
            k, v = item.split(':')
            self.datafields[k] = v
            
    def Reset(self):
        self.datafields = {}      

        
n_valid = 0
n_invalid = 1
with open('input.txt') as f:
    checker = PassportValidator()
    for line in f:
        if line.strip()=='':
            if checker.IsValid():
                n_valid += 1
            else:
                n_invalid += 1
            checker.Reset()
        else:
            checker.AddBatchRow(line)
    if checker.IsValid():
        n_valid += 1
    else:
        n_invalid += 1
print (f"Part 1: {n_valid} have the right fields, {n_invalid} do not" )  


class AdvancedValidator(PassportValidator):
    
    HEIGHT_REGEXP = re.compile("(\d+)(cm|in)")
    HAIR_REGEXP = re.compile("^#[0-9a-f]{6}")
    EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    PID_REGEXP = re.compile("^\d{9}$")

    def _validateBirthYear(self, value):
        return 1920 <= int(value) <= 2002
    def _validateIssueYear(self, value):
        return 2010 <= int(value) <= 2020
    def _validateExpYear(self, value):
        return 2020 <= int(value) <= 2030
    def _validateHeight(self, value):
        match = AdvancedValidator.HEIGHT_REGEXP.match(value)
        if AdvancedValidator.HEIGHT_REGEXP.match(value) is not None:
            if match[2]=="cm":
                return 150 <= int(match[1]) <= 193
            else:
                return 59 <= int(match[1]) <= 76
        return False
    def _validateHair(self, value):
        return AdvancedValidator.HAIR_REGEXP.match(value) is not None
    def _validateEyes(self, value):
        return value in AdvancedValidator.EYE_COLORS
    def _validatePid(self, value):
        return AdvancedValidator.PID_REGEXP.match(value) is not None

    def _validateItem(self, key):
        if key == 'byr':
            return self._validateBirthYear(self.datafields[key])
        elif key == 'iyr':
            return self._validateIssueYear(self.datafields[key])
        elif key == 'eyr':
            return self._validateExpYear(self.datafields[key])
        elif key == 'hgt':
            return self._validateHeight(self.datafields[key])
        elif key == 'hcl':
            return self._validateHair(self.datafields[key])
        elif key == 'ecl':
            return self._validateEyes(self.datafields[key])
        elif key == 'pid':
            return self._validatePid(self.datafields[key])
                
    def IsValid(self):
        for f in AdvancedValidator.REQUIRED_FIELDS:
            if f not in self.datafields.keys():
                return False
            if not self._validateItem(f):
                return False
        return True
            
        
n_valid = 0
n_invalid = 0
with open('/home/harry/notebooks/advent_of_code/day_04/input.txt') as f:
    checker = AdvancedValidator()
    for line in f:
        if line.strip()=='':
            if checker.IsValid():
                n_valid += 1
            else:
                n_invalid += 1
            checker.Reset()
        else:
            checker.AddBatchRow(line)
        
    if checker.IsValid():
        n_valid += 1
    else:
        n_invalid += 1

print (f"Part 2: {n_valid} have the right fields and data, {n_invalid} do not" )  

