#The merge_subdomains() function takes a list of subdomains as input and returns a merged list of unique subdomains. 
#It uses a try-except block to catch errors caused by invalid subdomains. 
#It splits each subdomain string into domain name and TLD parts and merges subdomains only if they have the same domain name and TLD. #
#It then uses a list comprehension to create the merged list directly.



#The get_subdomains_for_domain() function takes a domain name and a list of subdomains as input and returns a list of subdomains that belong to that domain. 
#It searches the input list for subdomains that end with the specified domain name.



#The input subdomains list contains subdomains with different TLDs and invalid subdomains for testing purposes.

#The script calls the merge_subdomains() function to create the merged list and prints it.

#The script calls the get_subdomains_for_domain() function to find all subdomains that belong to the "example.com" domain and prints them.

def merge_subdomains(subdomains):
    merged_subdomains = {}
    for subdomain in subdomains:
        try:
            domain_name, tld = subdomain.split(".")[-2:]
            merged_subdomains.setdefault(domain_name + "." + tld, set()).add(subdomain)
        except (ValueError, IndexError):
            print(f"Ignoring invalid subdomain: {subdomain}")

    merged_list = [subdomain for subdomains in merged_subdomains.values() for subdomain in subdomains]
    return merged_list


def get_subdomains_for_domain(domain_name, subdomains):
    subdomains_for_domain = []
    for subdomain in subdomains:
        if subdomain.endswith(domain_name):
            subdomains_for_domain.append(subdomain)
    return subdomains_for_domain


subdomains = [
    "subdomain1.example.com",
    "subdomain2.example.com",
    "subdomain1.example.net",
    "subdomain3.example.com",
    "subdomain2.example.net",
    "subdomain4.example.com",
    "invalid_subdomain",
    "subdomain.with.multiple.dots.com"
]

merged_list = merge_subdomains(subdomains)
print(merged_list)

example_subdomains = get_subdomains_for_domain("example.com", merged_list)
print(example_subdomains)
