import datetime


class Passport:
    """
    A class to represent a passport.

    Attributes:
    ----------
    passport_id : int
        A class attribute that assigns a unique ID to each passport.
    fname : str
        First name of the passport holder.
    lname : str
        Last name of the passport holder.
    dob : datetime.date
        Date of birth of the passport holder.
    country : str
        Country of issue of the passport.
    exp_date : datetime.date
        Expiry date of the passport.
    count_of_visit : dict
        A dictionary to track the number of visits to different countries.
    """

    # Initialise a unique identifier for each passport
    passport_id = 0

    def __init__(self, first_name, last_name, dob, country, exp_date):
        """
        Initialise the Passport object with holder's details.

        Parameters:
        ----------
        first_name : str
            First name of the passport holder.
        last_name : str
            Last name of the passport holder.
        dob : str
            Date of birth in ISO format (YYYY-MM-DD).
        country : str
            Country of issue of the passport.
        exp_date : str
            Passport expiration date in ISO format (YYYY-MM-DD).
        """

        self.fname = first_name
        self.lname = last_name
        self.dob = datetime.date.fromisoformat(dob)
        self.country = country
        self.exp_date = datetime.date.fromisoformat(exp_date)

        # Assign a unique passport ID
        self.passport_id = Passport.passport_id
        Passport.passport_id += 1

        # Initialize the count of visits to different countries
        self.count_of_visit = {}

    def summary(self):
        """
        Provides a summary of the passport details, including its validity.

        Returns:
        -------
        str
            A string summarising passport holder's details and validity.
        """

        if self.is_valid():
            validity = "It is valid."
        else:
            validity = "It is invalid."           

        # Print appropriate summary containing name, DOB and country of the passport holder along with the validity.
        return (f"This passport belongs to {self.fname} {self.lname} born on {self.dob} in {self.country}. {validity}")

    def is_valid(self):
        """
        Checks if the passport is still valid based on the expiration date.

        Returns:
        -------
        bool
            True if the passport is valid, False otherwise.
        """

        if self.exp_date > datetime.date.today():
            return True
        else:
            return False

    def check_data(self, first_name, last_name, dob, country):
        """
        Verifies if the provided data matches the passport details.

        Parameters:
        ----------
        first_name : str
            First name to check.
        last_name : str
            Last name to check.
        dob : str
            Date of birth to check in ISO format (YYYY-MM-DD).
        country : str
            Country of issue to check.

        Returns:
        -------
        bool
            True if all the provided details match and the passport is valid, otherwise False.
        """

        dob = datetime.date.fromisoformat(dob)
        if first_name == self.fname and last_name == self.lname and dob == self.dob and country == self.country:
            if self.is_valid():
                return True
            else:
                return False
        else:
            return False

    def stamp(self, country_name):
        """
        Records a visit to a new country, updating the visit count.

        Parameters:
        ----------
        country_name : str
            Name of the country visited.
        """

        # If country is same as country of issue of passport, do nothing
        if country_name == self.country:
            pass

        # If another country, then keep track of count of visit
        else:
            if country_name in self.count_of_visit:
                self.count_of_visit[country_name] += 1
            else:
                self.count_of_visit[country_name] = 1

    def countries_visited(self):
        """
        Lists all the countries the passport holder has visited.

        Returns:
        -------
        list
            A list of country names the passport holder has visited.
        """

        # Initialise a list to store all the visited country names
        self.list_of_countries = []
        for country_name in self.count_of_visit:
            self.list_of_countries.append(country_name)
        return self.list_of_countries

    def times_visited(self, country_name):
        """
        Returns the number of times the passport holder has visited a particular country.

        Parameters:
        ----------
        country_name : str
            The country name to check visits for.

        Returns:
        -------
        int
            Number of visits to the specified country.
        """

        if country_name in self.count_of_visit:
            return self.count_of_visit[country_name]
        else:
            return 0


    def sum_square_visits(self):
        """
        Calculates the sum of the squares of the number of visits to each country.

        Returns:
        -------
        int
            The sum of squares of visit counts.
        """

        answer = 0
        answer += sum(count ** 2 for count in self.count_of_visit.values())
        return answer

    def passport_number(self):
        """
        Returns the unique passport ID.

        Returns:
        -------
        int
            Passport ID number.
        """

        return self.passport_id


# Example usage of the Passport class
def main():
    """
    Main function to demonstrate the use of the Passport class.
    """

    # Creating passport objects
    alan = Passport("Alan", "Turing", "1912-06-23", "The United Kingdom", "2999-12-31")
    guido = Passport("Guido", "van Rossum", "1956-01-31", "The Netherlands", "1999-03-20")
    sam = Passport("Sam", "Hook", "1990-12-09", "Germany", "2030-06-19")

    # Printing passport summary of alan
    print(alan.summary())

    # Stamping passport for travel
    alan.stamp("Germany")
    alan.stamp("Germany")
    alan.stamp("The United Kingdom")    # home country scenario
    alan.stamp("Netherlands")

    sam.stamp("Germany")
    sam.stamp("Italy")
    sam.stamp("USA")
    sam.stamp("Canada")
    sam.stamp("USA")

    # Printing travel details of alan
    print(f"Countries visited: {alan.countries_visited()}")
    print(f"Times visited Germany: {alan.times_visited('Germany')}")
    print(f"Sum of square of visits: {alan.sum_square_visits()}")

    # Printing passport summary of guido showing validity
    print(guido.summary())

    # Printing passport summary of sam
    print(sam.summary())

    # Printing travel details of sam
    print(f"Countries visited: {sam.countries_visited()}")
    print(f"Times visited USA: {sam.times_visited('USA')}")
    print(f"Times visited Italy: {sam.times_visited('Italy')}")
    print(f"Sum of square of visits: {sam.sum_square_visits()}")


if __name__ == "__main__":
    main()
