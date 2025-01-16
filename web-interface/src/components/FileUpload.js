import React, { useState } from 'react';
import { uploadFile } from '../services/apiService';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setUploadStatus('Uploading...');
    
    const response = await uploadFile(file);
    
    if (response.success) {
      setUploadStatus('Upload successful!');
    } else {
      setUploadStatus('Upload failed.');
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      <p>{uploadStatus}</p>
    </div>
  );
};

export default FileUpload;
