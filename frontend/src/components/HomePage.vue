<template>
  <div class="p-4">
    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="language" class="block">Choose Interview Language:</label>
        <select id="language" v-model="formData.language" class="mt-1">
          <option value="en">English</option>
          <option value="zh">Simplified Chinese</option>
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
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'HomePage',
  setup() {
    const formData = ref({
      language: 'en',
      cv: null,
      jobDescription: null,
    })

    const handleFileChange = (field, event) => {
      formData.value[field] = event.target.files[0]
    }

    const submitForm = async () => {
      const data = new FormData()
      data.append('language', formData.value.language)
      data.append('cv', formData.value.cv)
      data.append('job_description', formData.value.jobDescription)
      
      try {
        await axios.post('/api/upload/', data, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        // Handle success here
        alert('Upload successful')
      } catch (error) {
        // Handle error here
        alert('Upload failed')
      }
    }

    return { formData, handleFileChange, submitForm }
  },
}
</script>
