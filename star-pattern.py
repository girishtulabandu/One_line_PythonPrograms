"""
Python One Liner for a star pattern
*                                                                                                                                      
* *                                                                                                                                    
* * *                                                                                                                                  
* * * *                                                                                                                                
* * * * * 

Input format-> pattern(5)
"""
pattern = lambda x: '\n'.join('* ' * i for i in range(x+1))
