import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    #dictionary of abbreviation keys for cities
    city_abbr = {'ch':'chicago',
                 'ny':'new york city',
                 'wa':'washington'}
    
    #dictionary of abbreviation keys for months
    month_abbr = {'jan':'january',
                  'feb':'february',
                  'mar':'march',
                  'apr':'april',
                  'may':'may',
                  'jun':'june',
                  'all':'all'}
    
    #dictionary of abbreviation keys for days
    day_abbr = {'mon':'monday',
                'tues':'tuesday',
                'wed':'wedneaday',
                'thur':'thursday',
                'fri':'friday',
                'sat':'saturday',
                'sun':'sunday',
                'all':'all'}
    
    #show abbreviation list of cities
    print('Hello! Let\'s explore some US bikeshare data!')
    print('City abbreviations')
    print('Chicago:CH \nNew York: NY \nWashington: WA')
    print('-'*40)
       
    #set variables for city, month, and day to empty strings
    city = '' 
    month = ''
    day = ''
                 
    #get user input for city (chicago, new york city, washington).
    while city not in city_abbr:
        city = input("Type abbreviated name of the city you wish to analyse:").lower()
    
    #show abbreviation list of months
    print('Month abbreviations')
    print('January:jan \nFebruary: feb \nMarch: mar \nApril:apr \nMay:may \nJune:jun')
    print('-'*40)
    
    #get user input for month
    while month not in month_abbr:
        month = input("Type the abbreviation of the month you wish to filter, or type 'all' to apply no month filter:").lower()
    
    #show abbreviation list of days
    print('Week day abbreviations')
    print('Monday:mon \nTuesday: tues \nWednesday: wed \nThursday:Thurs \nFriday:fri \nSaturday:sat \nSunday:sun')
    print('-'*40)   
    
    #get user input for day
    while day not in day_abbr:
        day = input("Type the abbreviation of the day of the week you wish to filter, or type 'all' to apply no month filter:").lower()
        
    #set city, month, and day variables to dictionary values of user input keys
    city = city_abbr[city]
    month = month_abbr[month]
    day = day_abbr[day]
    
    #print user options as input feedback
    print('Analysis for the following filtered parameters:')
    print('City:', city, '\nMonth:', month, '\nDay:', day)


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
    
    #read the city data into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the start time value to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #create new columns for the month, day, and hour of the data frame
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    
    #return the resulting data frame
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #list of months from january to june
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    
    # display the most common month using the mode function and displaying the first value
    common_month = df['Month'].mode()[0]
    print('The most common month is', months[common_month-1])

    # display the most common day of week using the mode function and displaying the first value
    common_day = df['Day'].mode()[0]
    print('The most common day is', common_day)

    # display the most common start hour using the mode function and displaying the first value
    common_start_hour = df['Hour'].mode()[0]
    print('The most common start time is', common_start_hour)

    #calculate how long it took the function to run
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station using the mode function and displaying the first value
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station:', common_start_station)

    #display most commonly used end station using the mode function and displaying the first value
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station:', common_end_station)

    #create new column that combines start and end stations
    df['Start-End'] = df['Start Station'].map(str) + ' - ' + df['End Station'].map(str)
    #display most frequent combination of start station and end station trip using the mode function and displaying the first value
    common_start_end = df['Start-End'].mode()[0]
    print('Most frequent combination of start and end stations:', common_start_end)

    #calculate how long it took the function to run
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time using the sum function
    total_duration_time = int(df['Trip Duration'].sum())
    #convert seconds to days, hurs, minutes, and seconds
    total_duration_time = str(datetime.timedelta(seconds=total_duration_time))
    print('Total travel time:', total_duration_time)

    #display mean travel time using the mean function
    avg_travel_time = int(df['Trip Duration'].mean())
    #convert seconds to days, hurs, minutes, and seconds
    avg_travel_time = str(datetime.timedelta(seconds=avg_travel_time))
    print('Average travel time:', avg_travel_time)

    #calculate how long it took the function to run
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user type using the value_counts function
    user_type = df['User Type'].value_counts()
    print("User types:")
    print(user_type)


    #Display counts of gender
    print('The following are the counts of Male and Female users:')
    #use try except block to catch errors from lack of data
    try:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    except:
        print('No gender info available')


    #Display earliest, most recent, and most common year of birth
    #use try except block to catch errors from lack of data
    try:
        YOB_earliest = int(df['Birth Year'].min())
        YOB_recent = int(df['Birth Year'].max())
        YOB_common = int(df['Birth Year'].mode()[0])
    
        print('Earliest birth year:',YOB_earliest)
        print('Most recent birth year:',YOB_recent) 
        print('Most common birth year:',YOB_common)
    except:
        print('No birth year info available')

    # calculate how long it took the function to run
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #option to see more stats or not
        time = input('\nWould you like to see the time stats? Enter yes or no.\n')
        if time.lower() == 'yes':
           time_stats(df)

        #Ask user if they want to view records of trip duration
        see_more_5 = input('\nWould you like to see the first 5 rows of trip duration data? Enter yes or no.\n')
        if see_more.lower() == 'yes':
           print(df['Trip Duration'].head(5))
        
        see_more_10 = input('\nWould you like to see another 5 rows of trip duration data? Enter yes or no.\n')
        if see_more.lower() == 'yes':
           print(df['Trip Duration'].head(10))

        #option to see more stats or not
        station = input('\nWould you like to see the station stats? Enter yes or no.\n')
        if station.lower() == 'yes':
            station_stats(df)
        #option to see more stats or not  
        duration = input('\nWould you like to see the trip duration stats? Enter yes or no.\n')
        if duration.lower() == 'yes':
            trip_duration_stats(df)
        #option to see more stats or not    
        user = input('\nWould you like to see the user stats? Enter yes or no.\n')
        if user.lower() == 'yes':
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
