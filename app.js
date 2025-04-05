const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

// Connect to MongoDB (Replace with your MongoDB URI)
mongoose.connect("mongodb://127.0.0.1:27017/snakeGame", { useNewUrlParser: true, useUnifiedTopology: true });

const scoreSchema = new mongoose.Schema({ score: Number });
const Score = mongoose.model("Score", scoreSchema);

// Store score
app.post("/score", async (req, res) => {
    const newScore = new Score({ score: req.body.score });
    await newScore.save();
    res.send("Score saved!");
});

// Fetch top scores
app.get("/leaderboard", async (req, res) => {
    const scores = await Score.find().sort({ score: -1 }).limit(5);
    res.json(scores);
});

app.listen(3000, () => console.log("Server running on port 3000"));
