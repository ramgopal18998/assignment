const app = new Vue({
    el: "#app",
    created: function() {
      this.fetchData();
    },
    computed: {
      
    },
    data: function() {
      return {
        isLoading: true,
        searchText: '',
        users: [
        ]
      }
    },
    methods: {
      filteredData: function() {
        var self = this;
        
        if(self.searchText != '') {
          var searchText =  self.searchText.toLowerCase();
          var data =  self.users.filter(function(obj, index) {
            return obj.name.toLowerCase().indexOf(searchText) != -1 || obj.position.toLowerCase().indexOf(searchText) != -1 || obj.about.toLowerCase().indexOf(searchText) != -1;
          });
          return data;
        }
        else {
          return self.users;
        }
      },
      fetchData: function() {
        var self = this;
        setTimeout(function() {
          self.users = [
            {
            name: 'Brijesh Kumar',
            position: 'Full stack Developer',
              linkedin: "https://www.linkedin.com/in/brijesh-kumar-a8a617a1/",
            about: 'This is Birjesh kumar, A full stack developer but interested in ui designs also. You can find me on linkedin.'
          },
           {
            name: 'Amrendra Dubey',
            position: 'Full stack Developer',
             linkedin: '',
            about: 'Hi, I am fullstack developer, willing to work remotely, let me know if you have an opportunity for me.'
          },
            {
            name: 'Ravi Jain',
            position: 'Full stack Developer',
              linkedin: '',
            about: 'Hi, I am Ravi Jain. I am full stack developer. I like to work with mysql and other database languages. You can reach out to me at any time at linkedin.'
          }
          ];
          self.isLoading = false;
        },1000);
        
      }
    }
  });

