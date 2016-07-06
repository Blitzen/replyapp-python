This readme will be updated over time.

ReplyApp: http://replyapp.io
ReplyApp api docs: http://support.replyapp.io/category/46-api

EXAMPLES:

    from replyapp import ReplyApp
    ra = ReplyApp('Api_Key')

    #ACTIONS:
    #Mark person as replied
    ra.actions.markasreplied(method='POST', data={'email': 'name@company.com'})
    ra.actions.markasreplied(method='POST', data={'domain': 'company.com'})

    #Push person to the campaign
    ra.actions.pushtocampaign(method='POST', data={'campaignId': 121, 'email': 'name@company.com'})

    #Add person and push to campaign
    data = {
        "campaignId": 121,
        "email": "name@company.com",
         "firstName": "James",
         "lastName": "Smith",
         "company": "Global Tech",
         "city": "San Francisco",
         "state": "CA",
         "country": "US",
         "title": "VP off Marketing"
     }
    ra.actions.addandpushtocampaign(method='POST', data=data)

    #Remove person from campaign by Id
    ra.actions.removepersonfromcampaignbyid(method='POST', data={'campaignId': 121, 'email': 'name@company.com'})

    #Remove person from all campaigns
    ra.actions.removepersonfromallcampaigns(method='POST', data={'email': 'name@company.com'})

    #People
    #Listing people
    ra.people()

    #Getting people from id
    ra.people.{{ID}}()
    #Getting people from email
    ra.people(data={'email': 'name@company.com'})

    #Saving people
    ra.people(method='POST', data={'id': 2232, 'email': james@globaltech.com', 'firstName': 'James', 'lastName': 'Smith', 'company': 'Global Tech', 'title': 'VP of Marketing'})

    #Deleting people
    ra.people(method='DELETE', data={'email': 'name@company.com'})
    ra.people.{{ID}}(method='DELETE')

    #Campaigns
    #Listing campaigns
    ra.campaigns()

    #Getting Campaigns
    ra.campaigns.{{ID}}()
    ra.campaigns(data={'name': 'Name Of Campaigns'})

    #Email Accounts
    #Listing Email Accounts
    ra.emailAccounts()