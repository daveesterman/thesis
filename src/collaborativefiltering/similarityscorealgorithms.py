'''
A group of classes which represent different ways of calculating
a similarity score between users for the purpose of collaborative
filtering.

Created on Sep 10, 2013

@author: dave
'''

from numpy import linalg as LA

class EuclidianDistance:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def score(self, vec1, vec2):
        '''Calculate similarity score between user 1 and user 2.
        
        Vectors must have all the same "components".  This means that we are
        comparing two users only on the items for which they both have a valid
        preference.  For example,
        
        if user1's vector = [4x, 5y, 6z],and 
           user2's vector = [10y, 15z], then   
           vec1 = [5y, 6z], and
           vec2 = [10y, 15z]
        because although user1 has a valid preference for x, user2 does not.
        
        
        Arguments:
        vec1 -- numpy array representing user 1's position in preference space
        vec2 -- numpy array representing user 2's position in preference space
        
        Return:
        numpy.float64 -- a value in range (0,1].  1 represents an exact match
                 between the users in preference space.  Lesser values are 
                 worse matches.
                 
        '''
        
        # Calculate the norm of the element-wise difference between the 
        # vectors.  This is the distance between the points.
        d = LA.norm(vec1 - vec2)
        # use d squared for compatibility with O'Reilly PCI
        score = 1.0 / (1.0 + d*d)
        return score
