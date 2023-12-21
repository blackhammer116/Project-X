import React from "react";
import { FaFile } from "react-icons/fa";
import { FaTrash } from "react-icons/fa";
import Header from "./header.css";
import icon1 from "./icon1.jpg";
import axios from "axios";
import { URL, getKeyByValue } from "./Constants";

export default function Main() {
  const [result, setResult] = React.useState(null);
  const [result1, setResult1] = React.useState(null);
  const [file, setFile] = React.useState(null);
  const [message, setMessage] = React.useState("");
  const [passPhrase, setPassPhrase] = React.useState("");
  const handleChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handelDelete = () => {
    setFile(null);
  };

  const handleClickDecryptMsg = async () => {
    const response = await axios.post(`${URL}/d_text`, { message, passPhrase });
    const res = response.data;
    setResult1(res.normal_text);
  };
  const handleClickEncryptMsg = async () => {
    const response = await axios.post(`${URL}/e_text`, { message, passPhrase });
    const res = response.data.utf8Data;
    setResult1(res.cypher_text);
  };

  const handleClickEncryptFile = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const response = await axios.post(`${URL}/encrypt_file`, {
      formData,
      passPhrase,
    });
    const res = response.data;
    setResult(res.encrypted_file_path);
  };

  const handleClickDecryptFile = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const response = await axios.post(`${URL}/decrypt_file`, {
      formData,
      passPhrase,
    });
    const res = response.data;
    setResult(res.decrypted_file_path);
  };

  return (
    <div className="main-container">
      <img src={icon1} className="main-img" />
      <div className="main-msg">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>

        {!result && (
          <textarea
            className="main-textarea"
            name="message"
            onChange={(e) => {
              setMessage(e.target.value);
            }}
          ></textarea>
        )}

        {result && (
          <div className="result-zone">
            <h1>Your Message:</h1>
            <h2>{result1}</h2>
          </div>
        )}

        <input
          type="text"
          name="passPhrase"
          onChange={(e) => {
            setPassPhrase(e.target.value);
          }}
          className="main-pass"
          placeholder="Enter A PassPhrase"
        />
        <div className="main-buttons">
          <button className="main-btn" onClick={handleClickEncryptMsg}>
            Encrypt
          </button>
          <button className="main-btn" onClick={handleClickDecryptMsg}>
            Decrypt
          </button>
        </div>
      </div>

      <div className="main-file">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.{" "}
        </p>
        <input
          type="text"
          name="passPhrase"
          onChange={(e) => {
            setPassPhrase(e.target.value);
          }}
          className="main-pass"
          placeholder="Enter A PassPhrase"
          required
        />
        <br />

        {file && (
          <div className="file-btn">
            <ul>
              <li>
                <FaFile className="file" />
                <p className="file-name">{file.name}</p>{" "}
                <FaTrash className="trash" onClick={handelDelete} />
              </li>
            </ul>
          </div>
        )}
        {!file && (
          <input type="file" onChange={handleChange} className="file-upload" />
        )}

        <div className="main-buttons">
          <button className="main-btn" onClick={handleClickEncryptFile}>
            Encrypt
          </button>
          <button className="main-btn" onClick={handleClickDecryptFile}>
            Decrypt
          </button>
        </div>
      </div>
    </div>
  );
}
