#include <bits/stdc++.h>
using namespace std;

struct node{
	int data;
	node* left;
	node* right;
};

node* newNode(int data)
{
	node* temp_node = new node;
	temp_node->data = data;
	temp_node->left = NULL;
	temp_node->right = NULL;
	return temp_node;
}
void BFS(node* root)
{
	if(root == NULL)
		return;
	queue<node *> q;
	q.push(root);
	while(q.empty() == false)
	{
		node* temp_node = q.front();
		cout << temp_node->data << " ";
		q.pop();

		if(temp_node->left != NULL)
			q.push(temp_node->left);
		if(temp_node->right != NULL)
			q.push(temp_node->right);
	}
}
void Postorder(node* root)
{
	if(root == NULL)
		return;
	Postorder(root->left);
	Postorder(root->right);
	cout << root->data << " ";
}
void Inorder(node* root)
{
	if(root == NULL)
		return;
	Inorder(root->left);
	cout << root->data << " ";
	Inorder(root->right);
}
void Preorder(node* root)
{
	if(root == NULL)
		return;
	cout << root->data << " ";
	Preorder(root->left);
	Inorder(root->right);
}
void TreeHeight(node* root)
{
	if(root == NULL)
		return 0;
	queue<node *> q;
	q.push(root);

	int height = 0;
	while(1)
	{
		int nodeCount = q.size();
		if(nodeCount == 0)
			return height;
		height++;
		while(nodeCount > 0)
		{
			node* temp_node = q.front();
			q.pop();

			if(temp_node->left != NULL)
				q.push(temp_node->left);
			if(temp_node->right != NULL)
				q.push(temp_node->right);
			nodeCount--;
		}
	}
}
int main()
{
	node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	cout << "BFS" << endl;
	BFS(root);
	cout << endl << "DFS Preorder" << endl;
	Preorder(root);
	cout << endl << "DFS Inorder" << endl;
	Inorder(root);
	cout << endl << "DFS Postorder" << endl;
	Postorder(root);
	cout << endl << "Tree Height" << endl;
	cout << TreeHeight(root);
	return 0;
}