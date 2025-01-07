import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8015/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 120000, // 30 seconds
});

export const sendMessage = async (message) => {
  try {
    // Send as JSON body instead of URL params
    const response = await api.post('/chat', {
      question: message
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      console.log('Error response:', error.response.data);
      const errorMessage = error.response.data.detail || 
                          error.response.data.message || 
                          'Server error';
      throw new Error(errorMessage);
    } else if (error.request) {
      throw new Error('No response from server. Please check your connection.');
    } else {
      throw new Error('An unexpected error occurred');
    }
  }
};

// Optionally add request/response interceptors for global handling
api.interceptors.request.use(
  (config) => {
    // You can add auth tokens here if needed
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Global error handling
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);
