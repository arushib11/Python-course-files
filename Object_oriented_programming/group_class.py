# Create a group class with methods add(),delete() and get_members()

class Group:
    def __init__(self,group_name,grp_members=[]):
        self.group_name=group_name
        self.grp_members=grp_members

    def add(self,new_name):
        self.grp_members.append(new_name)
    
    def delete(self,del_name):
        if del_name not in self.grp_members:
            raise Exception("Member not in group")
        else: 
            self.grp_members.remove(del_name)
    
    def get_members(self):
        sorted_grp_members=sorted(self.grp_members)
        return sorted_grp_members
    
    def merge(self,group):
        new_lst=group.grp_members+self.grp_members
        new_group=Group("any name",new_lst)
        return new_group