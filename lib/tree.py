class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        return self._search_by_id(self.root, target_id)

    def _search_by_id(self, node, target_id):
        if node['id'] == target_id:
            return node
        for child in node['children']:
            result = self._search_by_id(child, target_id)
            if result:
                return result
        return None
