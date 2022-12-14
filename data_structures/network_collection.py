import ipaddress
from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipv4_network
        self.entries = [Entry(entry['address'], entry['available'], entry['last_used'])
                        for entry in raw_entry_list]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        network = ipaddress.ip_network(self.ipv4_network)
        valid_entries = []

        for entry in self.entries:
            address = getattr(entry, 'address')

            try:
                valid_address = ipaddress.IPv4Address(address)
            except ValueError:
                continue

            if valid_address in network:
                valid_entries.append(entry)

        self.entries = valid_entries

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        self.entries = sorted(self.entries)
