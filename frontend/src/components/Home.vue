<template>
    <div class="p-4">
      <form @submit.prevent="submitForm" class="space-y-4">
        <div>
          <label for="language" class="block">Choose Interview Language:</label>
          <select id="language" v-model="formData.language" class="mt-1">
            <option value="en">English</option>
            <option value="zh-hans">Simplified Chinese</option>
          </select>
        </div>
        <div>
          <label for="cv">Upload Your CV:</label>
          <input type="file" id="cv" @change="handleFileChange('cv', $event)" />
        </div>
        <div>
          <label for="jobDescription">Upload Job Description:</label>
          <input type="file" id="jobDescription" @change="handleFileChange('jobDescription', $event)" />
        </div>
        <button type="submit" class="px-4 py-2 bg-blue-500 text-white">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        formData: {
          language: 'en',
          cv: null,
          jobDescription: null,
        },
      };
    },
    methods: {
      handleFileChange(field, event) {
        this.formData[field] = event.target.files[0];
      },
      async submitForm() {
        const formData = new FormData();
        formData.append('language', this.formData.language);
        formData.append('cv', this.formData.cv);
        formData.append('job_description', this.formData.jobDescription);
        
        try {
          await this.$axios.post('/api/upload/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
          // Handle success
        } catch (error) {
          // Handle error
        }
      },
    },
  };
  </script>
