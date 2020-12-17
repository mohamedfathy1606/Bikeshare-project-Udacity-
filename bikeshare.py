import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Validate the user input using while loop.
    while True:
        try:
            city_selection = input('to view the availble bikeshare data, type:\n (a) for chicago\n (b) for new york city\n (c) for washington\n ').lower()
            if city_selection in ['a','b','c']:
                break
        # I have used the KeyboardInterrupt error in the except statement because some users may use it to quit. But if the users input was anything other than'a' or 'b' or 'c' then show invalid message and input again
        except keyboardinterrupt:
            print('\nNO input taken!')
        else:
            print('invalid city choice!!')
            
    city_selections = {"a":"chicago", "b":"new york city", "c":"washington"}
    if city_selection in city_selections.keys():
        city = city_selections[city_selection]
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    
    month = input('\nTo filter {}\'s data by a prticular month, please type the month or all for not filtering any month:\n-January\n-February\n-March\n-April\n-May\n-June\nAll\n\n:'.format(city.title())).lower()

    # Validate the user input using while loop.
    while month not in months:
        print("that's invalid choice, please type a valid month name or all")
        
        month = input('\nTo filter {}\'s data by a prticular month, please type the month or all for not filtering any month:\n-January\n-February\n-March\n-April\n-May\n-June\nAll\n\n:'.format(city.title())).lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\n\nTo filter {}\s data by a particular day, please type the day or all for not filtering a day:\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n\n:'.format(city.title())).lower()
    # Validate the user input using while loop.
    while day not in days:
        print("that's invalid choice, please type a valid day name or all")
        
        day = input('\n\nTo filter {}\s data by a particular day, please type the day or all for not filtering a day:\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n\n:'.format(city.title())).lower()
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # first loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # second convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # then extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # then filter by month if applicable

    if month != 'all':
        # creating a dict useing the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # then filtering by month to create the new dataframe
        df = df[df['month'] == month]
        
       # again filter by day of week if applicable
    if day != 'all':
        # then filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """
    Here we are going to Answer questions about Popular times of travel
    and will divide our data to three questions.
    1- most common month.
    2- most common day of week.
    3-most common hour of day.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('common month:', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('common day of week:', common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Here we are going to Answer questions about Popular stations and trip
    and will divide our data to three questions.
    1- most common start station.
    2- most common end station.
    3-most common trip from start to end (i.e., most frequent combination of start station and end station).
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Commonly  start station: ', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Commonly  end station: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('Common start station and end station : ', common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Here we are going to Answer questions about Trip duration
    and will divide our data to two questions.
    1- Total travel time
    2- Average travel time.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time: ',mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Here we are going to Answer questions about User info
    and will divide our data to three questions.
    1- counts of each user type.
    2- counts of each gender (only available for NYC and Chicago).
    3-earliest, most recent, most common year of birth (only available for NYC and Chicago).
    
    """   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("The latest year of birth is " + str(latest) + "\n")
        most_common = df['Birth Year'].mode()[0]
        print ("The most frequent year of birth is " + str(most_common) + "\n")
        return earliest, latest, most_common
    except:
        print('There is no birth date data for Washington.')
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_raw_data(city):
    # print a message to inform user that there is more data 
    print('\nRaw data is availble to check...\n')
     # Then asking the user to hos\her input if would like to see more data or not
    display_raw = input('\nWould you like to see the raw data? Enter yes or no.\n')
    while display_raw == 'yes':
        try:
               # Here we use the function pd.read_csv() with the chunksize of 5 row display
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                # Then we repeat asking for input again.
                display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
                if display_raw != 'yes':# we want to get out of this loop if the answer is not 'yes'
                    print('Thank You')
                    break # here we get out of the for loop on the chunks
            break# then we get out of the enclosing while loop
            # I have used the KeyboardInterrupt error in the except statement because some users may use it to quit. But if the users input was anything other than 'yes' the loops also will be terminated.
        except KeyboardInterrupt:
            print('Thank you.')
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()