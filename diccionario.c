// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <cs50.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 100;

// Hash table
node *table[N];
int palabras = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashedWord = hash(word);

    node *n = table[hashedWord];

    while (n != NULL)
    {
        if (strcasecmp(n->word, word) == 0)
            return true;
        n = n -> next;
    }
    return false;
}

// Hashes word to a number (https://stackoverflow.com/questions/7666509/hash-function-for-string
unsigned int hash(const char *word)
{
   unsigned int hash = 0;
    for (int i = 0 ; word[i] != '\0' ; i++)
    {
        hash = 31*hash + word[i];
    }
    return hash % N;
}


// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    // Check if open succesfully
    if (file == NULL)
    {
        return false;
    }
    // Take in count /0
    char word[LENGTH + 1];
    while(fscanf(file, "%s\n", word) != EOF)
    {
        // New word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        int hashedWord = hash(word);
        // Insert on hash function
        if (table[hashedWord] == NULL)
            table[hashedWord] = n;
        else if (table[hashedWord])
        {
            n -> next = table[hashedWord];
            table[hashedWord] = n;
        }
        palabras++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return palabras;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for ( int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while(cursor != NULL)
        {
            node *tmp = cursor;
            // Advance cursor
            cursor = cursor -> next;
            // Free tmp
            free(tmp);
        }
        return true;
    }
    return false;
}