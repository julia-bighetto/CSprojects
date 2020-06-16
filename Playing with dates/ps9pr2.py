#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A class to represent calendar dates   
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####

    def tomorrow(self):
        """ changes the called object so it represents one calendar day after
        the date that it originally represented
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29
        month = days_in_month[self.month]
        self.day += 1
        if month == 31:
            if self.day == 32:
                if self.month == 12:
                    self.day = 1
                    self.month = 1
                    self.year += 1
                else:
                    self.day = 1
                    self.month += 1
        if month == 30:
            if self.day == 31:
                self.day = 1
                self.month += 1
        if month == 28:
            if self.day == 29:
                self.day = 1
                self.month += 1
        if month == 29:
            if self.day == 30:
                self.day = 1
                self.month += 1

    def add_n_days(self, n):
        """ changes the calling object so it represents n calendar days after
            the date it originally represented
        """
        print(self)
        for c in range(0, n):
            self.tomorrow()
            print(self)

    def __eq__(self, other):
        """ returns True if the called object self and the argument other represent
            the same calendar date. It returns False otherwise
        """
        if self.day == other.day:
            if self.month == other.month:
                if self.year == other.year:
                    return True
        return False

    def is_before(self, other):
        """ returns True if the called object represents a calendar date that occurs
            before the calendar date that is represented by other. If self and other
            represent the same day, or if self occurs after other, the method
            returns False
        """
        if self.year > other.year:
            return False
        if self.year < other.year:
            return True
        else:
            if self.month < other.month:
                return True
            if self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                else:
                    return False

    def is_after(self, other):
        """ returns True if the calling object represents a calendar date that
            occurs after the calendar date that is represented by other. If
            self and other represent the same day, or if self occurs before
            other, the method returns False
        """
        if self.year < other.year:
            return False
        if self.year > other.year:
            return True
        else:
            if self.month > other.month:
                return True
            if self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                else:
                    return False

    def diff(self, other):
        """ returns an integer that represents the number of days between self
            and other
        """
        date1 = self.copy()
        date2 = other.copy()
        if date1 == date2:          
            return 0
        if date1.is_before(date2) == True:
            count = 0
            while date1.is_before(date2) == True:
                date1.tomorrow()
                count += 1
            return count * -1
        else:
            if date2.is_before(date1) == True:
                newcount = 0
                while date2.is_before(date1) == True:
                    date2.tomorrow()
                    newcount += 1
                return newcount


    def day_of_week(self):
        """ returns a string that indicates the day of the week of the Date object
        """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
        date1 = Date(4, 3, 2017)
        numberofdays = self.diff(date1)
        variable = numberofdays % 7
        if variable == 0:
            return day_of_week_names[0]
        elif variable == 1:
            return day_of_week_names[1]
        elif variable == 2:
            return day_of_week_names[2]
        elif variable == 3:
            return day_of_week_names[3]
        elif variable == 4:
            return day_of_week_names[4]
        elif variable == 5:
            return day_of_week_names[5]
        elif variable == 6:
            return day_of_week_names[6]
