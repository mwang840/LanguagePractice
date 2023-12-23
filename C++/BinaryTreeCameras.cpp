#include <iostream>
using namespace std;
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


struct TreeNode {
    int val;
    TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

 int minCameraCover(TreeNode *root){
    
    if(root == NULL){
        return 1;
    }
    int totalCameras = 0;
    int left = minCameraCover(root->left);
    int right = minCameraCover(root->right);
    if(left == 1 && right == 1){
        return 2;
    }
    else if(left ==2 || right == 2){
        totalCameras++;
        return 3;
    }
    return 1;
 }


int main(){
    std::cout << "Hi";
}