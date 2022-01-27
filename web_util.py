import urllib3
import webbrowser

def open_linkedin(first_name, last_name):
    name = first_name + ' ' + last_name
    webbrowser.open_new_tab("https://www.linkedin.com/search/results/people/?keywords={0}&origin=CLUSTER_EXPANSION&sid=zWD".format(name) )

def open_crm(first_name, last_name):
    full_name = first_name+"+"+last_name
    base_url = 'https://diligence.crm3.dynamics.com/main.aspx?appid=83b84ff6-d36e-ea11-a811-000d3a0c94a6&pagetype=search&searchText={0}&searchType=1'.format(full_name)
    query = base_url.format(full_name)
    webbrowser.open_new_tab(query)
def inspect(client):
    first_name, last_name = client['First Name'].replace('?','e'), client['Last Name'].replace('?','e')
    try:
        company = client['Company']
        phone = client['Office Number']
    except:
        company = ""
        try:
            phone = client['Home Number']
        except:
            phone = client['Office Number']
    query = first_name + '+' + last_name + "+" + company
    webbrowser.open_new_tab("https://www.google.com/search?channel=fs&client=ubuntu&q={0}".format(query))
    webbrowser.open_new_tab("https://www.google.com/search?channel=fs&client=ubuntu&q={0}".format(phone))
    if company:
        webbrowser.open_new_tab("https://www.google.com/search?channel=fs&client=ubuntu&q={0}".format(company+' allbiz'))
    open_crm(first_name, last_name)