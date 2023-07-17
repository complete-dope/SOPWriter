#!/usr/bin/env python


from google_scholar import GoogleScholarUser

if __name__ == '__main__':
	user_id = 'iYN86KEAAAAJ' # The Google Scholar ID of the user you want to scrape
	# To retrieve this user_id, visit the profile of the user.
	# The user=xxxxxxxx part in the URL is the user_id you need.

	scraper = GoogleScholarUser(user_id)
	scraper.get_scholar_articles()
