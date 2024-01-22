import React from "react";
import { useNavigate } from "react-router-dom";
import { useRef, useState } from "react";
import axios from "axios";

import "./postWindow.css";

import ImageButton from "../ImageButton/ImageButton";
import AppButton from "../AppButton/AppButton";
import InputMedia from "../InputMedia/InputMedia";

function PostWindow(props) {
  const [acceptedFileType, setAcceptedFileType] = useState("image/*");

  const formData = new FormData(); //  Create FormData to add post details.

  const email = "spm@gmail.com"; // get from login session
  formData.append("email", email);

  // for navigation
  const navigate = useNavigate();

  // input media files - this in to trigger the file input click event.
  const fileInputRef = useRef(null);

  // Function to trigger file input click.
  const handleButtonClick = async (fileType) => {
    await setAcceptedFileType(fileType);
    console.log(fileType);
    if (fileInputRef.current) {
      fileInputRef.current.click(); // when button clicks this one is called, and the input one also clicked.
    }
  };
 
  const sendPostDataButtonClick = () => {
    
  };

  // To handle file input. This function will be triggered when a file is selected.
  const handleFileChange = (event) => {
    console.log("handleFileChange executed");
    console.log("pos0");
    const selectedFile = fileInputRef.current.files[0];

    console.log('Selected File:', selectedFile);


    if (selectedFile) {
      console.log("Selected File:", selectedFile);
      // Perform operations with the selected file (e.g., upload, display preview, etc.)
      formData.append("fileContent", selectedFile);
    }
  };

  // Post data to backend.
  const sendPostData = () => {
    console.log('FormData:', formData);
    console.log("pos");
    axios
      .post("http://localhost:5000/api/postfile/uploadfile", formData, {
        headers: {
          "Content-Type": "multipart/form-data", // Update content type
        },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((error) => {
        console.error("Error sending data:", error);
      });

    navigate("/profile_feed");
  };

  return (
    <div className="PostMainComponent">
      <div className="postContainer">
        <h2 className="createPost">Create Post</h2>
        <div className="postPreview">
          <div className="previewElement">
            <img src="./assets/card1.jpeg" className="imagePreview" alt=""></img>
          </div>
          <p className="note">Attach your resource</p>

          <div className="objectPicker">
            <ImageButton
              title="Photo"
              backgroundColor="black"
              imageLink="./assets/Photo.svg"
              handleClick={() => handleButtonClick("image/*")}
            ></ImageButton>

            <ImageButton
              title="Video"
              backgroundColor="black"
              imageLink="./assets/Video.svg"
              handleClick={() => handleButtonClick("video/*")}
            ></ImageButton>
            <ImageButton
              title="Code"
              backgroundColor="black"
              imageLink="./assets/Code.svg"
              handleClick={() => handleButtonClick("text/plain")}
            ></ImageButton>

            <ImageButton
              title="Object"
              backgroundColor="black"
              imageLink="./assets/Object.svg"
              handleClick={() => handleButtonClick(".obj")}
            ></ImageButton>
            <InputMedia
              handleFileChange={handleFileChange}
              fileInputRef={fileInputRef}
              acceptedFileTypes={acceptedFileType}
            ></InputMedia>
          </div>

          <AppButton
            title="Share to Cubers"
            className="shareBtn"
            onClickFunction={sendPostData}
          ></AppButton>
        </div>
      </div>
    </div>
  );
}

export default PostWindow;
