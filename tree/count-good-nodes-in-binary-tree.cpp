class Solution {
public:
    int goodNodes(TreeNode* root, int maxFromRoot=INT_MIN) {
        if(root == NULL) return NULL; 

        int count = 0;
        if(root->val >= maxFromRoot){ 
            count++;
            maxFromRoot = root->val;
        }
        count += goodNodes(root->left , maxFromRoot);
        count += goodNodes(root->right , maxFromRoot);
        return count;
    }
};
