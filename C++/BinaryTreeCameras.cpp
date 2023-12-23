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

int totalCameras = 0;
int minCameraCover(TreeNode *root);



int searchCamera(TreeNode *root){
     if(root == NULL){
        return 1;
    }
    int left = minCameraCover(root->left);
    int right = minCameraCover(root->right);
    if(left == 0 || right == 0){
        totalCameras++;
        return 2;
    }
    if(left == 1 && right == 1){
        return 0;
    }
}

int minCameraCover(TreeNode *root){
    int totalNodes = searchCamera(root);
    if(totalNodes == 0){
        return totalCameras + 1;
    }
    return totalCameras;
 }