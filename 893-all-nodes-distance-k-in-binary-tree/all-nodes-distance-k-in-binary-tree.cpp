/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_map<TreeNode*, TreeNode*> parentMap;
        buildParentMap(root, parentMap); // Step 1: Build parent links

        unordered_set<TreeNode*> visited; // Track visited nodes to avoid cycles
        queue<pair<TreeNode*, int>> q; // Queue for BFS with node and current distance
        q.push({target, 0}); // Start BFS from the target node
        visited.insert(target);

        vector<int> result; // Store nodes at distance k

        while (!q.empty()) {
            TreeNode* node = q.front().first;
            int dist = q.front().second;
            q.pop();

            // If current node is at distance k, add its value to the result
            if (dist == k) {
                result.push_back(node->val);
            } else if (dist < k) {
                // Traverse neighbors: left child, right child, and parent
                if (node->left && visited.find(node->left) == visited.end()) {
                    q.push({node->left, dist + 1});
                    visited.insert(node->left);
                }
                if (node->right && visited.find(node->right) == visited.end()) {
                    q.push({node->right, dist + 1});
                    visited.insert(node->right);
                }
                if (parentMap.count(node) && visited.find(parentMap[node]) == visited.end()) {
                    q.push({parentMap[node], dist + 1});
                    visited.insert(parentMap[node]);
                }
            }
        }

        return result; // Return nodes at distance k
    }

private:
    void buildParentMap(TreeNode* node, unordered_map<TreeNode*, TreeNode*>& parentMap) {
        if (!node) return;

        if (node->left) {
            parentMap[node->left] = node; // Link left child to its parent
            buildParentMap(node->left, parentMap);
        }

        if (node->right) {
            parentMap[node->right] = node; // Link right child to its parent
            buildParentMap(node->right, parentMap);
        }
    }
};