export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
  
    try {
      const response = await fetch('https://your-api-endpoint/upload', {
        method: 'POST',
        body: formData,
      });
  
      const result = await response.json();
      return result;
    } catch (error) {
      console.error('Error uploading file:', error);
      return { success: false };
    }
  };
  
