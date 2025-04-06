/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void traversal(TreeNode* root, vector <int> &tree)
    {
        if (root == NULL) return ;
        tree.push_back(root->val);
        traversal(root->left,tree);
        traversal(root->right,tree);

    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector <int> tree ;
        traversal(root,tree);
        return tree;
    }
};