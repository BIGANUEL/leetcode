from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        owner = {}

        # Find function with path compression
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function
        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Union emails in same account and map email → name
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union(first_email, email)
                owner[email] = name

        # Step 2: Group emails by root parent
        groups = defaultdict(list)
        for email in owner:
            root = find(email)
            groups[root].append(email)

        # Step 3: Prepare result
        result = []
        for emails in groups.values():
            result.append([owner[emails[0]]] + sorted(emails))
        return result
