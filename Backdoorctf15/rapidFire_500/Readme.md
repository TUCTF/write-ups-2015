This challenge was to solve a variety of questions in rapid succession.
You only have about 1 or 2 seconds to give the answer for each question, so manual net-catting is out.
You also have to answer the questions consecutively, any wrong answer kill your session and you have to start from the beginning.
By looking at the output, we see there are 11 different questions that can be asked, they are:
	1) the n'th prime number
	2) convert a base 10 number to binary
	3) sum the first n natural numbers (1,2,...)
	4) sum the first n odd natural numbers
	5) find the n'th digit of PI
	6) find the n'th Fibonacci number
	7) sum the first n Fibonacci numbers
	8) find the md5 hash of a given number
	9) find the name of a country for a given city
	10)find the 2 digit country code of a country
	11)find the release year of a given movie

Since there were clear key works to distinguish each case I simply looked for the phrase in the question and called the appropriate method for it.
This was written in python 2.x

1) the n'th prime number:
	the n's can be up to 1,000,000 so clearly we can't derive the prime list on the go.
	I found the first 1,000,000 primes and read those into a list.
	As a note, 0 and 1 are not considered primes

2) convert a base 10 number to binary:
	python has a built in binary converter.

3) sum the first n natural numbers:
	It is tempting to start with 'for i in range(n)', but when the n can be over 10 million, it is faster to use a formula.
	The formula for the sum of the first n numbers is: (n*(n+1))/2

4) sum the first n odd natural numbers:
	Again, a formula gives us the answer: n**2

5) find the n'th digit of PI
	since this asks for up to the 1,000,000'th digit, any sort of calculation will probably take too long. And there is a list of the first million digits of pi
	I just read this in as an array and selected the index
	As a note, the 0th digit is 3, the 1st digit is 1, and so on.

6) find the n'th Fibonacci number:
	There are some formulas for fib that are O(log(n)), but there is even a better solution. Find a list and import it.

7) sum the first n Fibonacci numbers
	Again, here for i in... is not the answer. Since we already have a list of fibs, we can grab any number at cost O(1).
	the sum of the first n is: fib(n+2) - 1 
		As a note, since we have the list, python's sum will get you the result quick enough, but this is the more elegant solution

8) find the md5 has of a given number:
	haslib has a md5 digest.

Now is when it gets tricky. The above always work, the methods below sometimes fail because of silly things
(like the Peoples Democratic Republic of Korea vs. North Korea, and Taiwan vs. China as examples)

9) find the name of a country for a given city:
	I was inspired by this project for this one https://github.com/ctfs/write-ups-2015/tree/master/0ctf-2015/misc/geo-newbie
	The idea is to use requests to search a website for a given city and select out the first country and return that value.
	It is easier to look at the comments in the code than to explain it here.
	Note: so countries are funny in that they aren't always well defined. There are some discrepancies, and it will sometimes fail here.

10) find the 2 digit country code of a country
	This is almost exactly what the project above was originally intended for, but I implemented a different method before I found that one.
	I used the package countrycode to look up the 2 digit code (iso2c) for a given country

11) find the release year of a given movie:
	I again turn to requests for this. IMDB will take API requests, and list all movies and release years for a given query.
	I used regex to find every string in the following format: (dddd) (where d is [0-9].
	Then return the first one in that list (the year of the closest match, latest year)
	This will also fail, because sometimes there are multiple releases of a given title, or the search will return actors and movies.

So after 200 question (really 199), you get:
flag:[redacted]
instead of a question.

As a general note, don't look at the code for the best programming practices.
This is written quick and dirty and then cleaned up a little for readability after it worked.
