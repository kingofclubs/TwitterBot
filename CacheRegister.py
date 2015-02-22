#check cache
class CacheRegister:
    activeDir = ''
    activeFileLocation = ''
    activeUser = {}
    activeFile = ''
    activeUserID = 0
    #cache file format
    #{userID: 'userName', 'cacheAge': lastUpdatedUnixTime,
    #'tweets': {tweetID: 'tweet content'}

    def __init__(self):
        CacheRegister.activeDir = 'cache/'
        CacheRegister.activeUser = {}
        CacheRegister.activeFile = ''
        print "CA-CHING"
        
    def setActiverUser(self, userID):
        self.activeUserID = userID
        self.activeFileLocation = self.activeDir + str(userID) +'.pkl'
        
    def checkCache(self, userID):
        fileLocation = self.activeDir + str(userID)+'.pkl'
        try:
            self.activeFile = open(fileLocation,'r')
            self.activeFile.close()
            return True
        except:
            print "Unable to locate cache file for user " + str(userID)
            return False
            
    def createCache(self, userID):
        import time, cPickle
        fileLocation = self.activeDir + str(userID)+'.pkl'
        print "Attempting to create cachefile"
        try:
            self.activeFile = open(fileLocation,'w+')
            self.activeUser = {userID: '', 'cacheAge': time.time(), 'tweets': {}}
            cPickle.dump(self.activeUser, self.activeFile)
            self.activeFile.close()
            return True
        except:
            print "Error: unable to create cache file"
            raise
            return False

    def deleteCache(self, userID):
        import os
        fileLocation = self.activeDir + str(userID)+'.pkl'
        try:
            os.remove(fileLocation)
            return True
        except:
            print "Error: unable to delete cache file"
            return False
    
    def loadCache(self, userID):
        import cPickle
        fileLocation = self.activeDir + str(userID)+'.pkl'
        try:
            self.activeFile = open(fileLocation, 'r')
            self.activeUser = cPickle.load(self.activeFile)
            self.activeFile.close()
            return True
        except:
            print "Unable to unload cache from user ID " + str(userID)
            return False

    def checkAgeCache(self, userID):
        import time
        currentTime = time.time()
        try:
            timeDiff = currentTime - self.activeUser['cacheAge']
            return timeDiff
        except:
            print "Unable to locate cacheAge from user id " + str(userID)
            return False
    
    def appendCache(self, userID, dictOfTweets):
        import time
        try:
            self.activeUser['tweets'].update(dictOfTweets)
            self.activeUser['cacheAge'] = time.time()
            return True
        except:
            raise
            print "Unable to append cache from user ID " + str(userID)
            return False
        
    def overwriteCache(self, userID):
        import cPickle
        fileLocation = self.activeDir + str(userID)+'.pkl'
        try:
            self.activeFile = open(fileLocation,'w')
            cPickle.dump(self.activeUser, self.activeFile)
            self.activeFile.close()
            return True
        except:
            print "Unable to overwrite cache from user ID " + str(userID)
            raise
            return False
            
        
