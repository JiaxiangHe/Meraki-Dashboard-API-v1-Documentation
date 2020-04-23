import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
license_id = '1234'
network_id = 'N_24329156'
seat_count = 20

response = dashboard.organizations.assignOrganizationLicensesSeats(
    organization_id, license_id, network_id, seat_count
)

print(response)