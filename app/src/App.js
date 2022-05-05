import React from "react";
import SelectLabels from "./components/SelectLabels";
import SelectGenre from "./components/SelectGenre";
import SelectMedia from "./components/SelectMedia";
import MyStepper from "./components/MyStepper";
import { pipeline } from "./API";
import { Container, Stack, Typography } from "@mui/material";

function App() {

  const [step, setStep] = React.useState(0);
  const [selections, setSelections] = React.useState(null);
  const [genres, setGenres] = React.useState(null);
  const [media, setMedia] = React.useState(null);

  const finishStepZero = async (country, media, time_period, rating, duration) => {
    let result = await pipeline(country, media, time_period, rating, duration, null);
    setSelections({"country": country, "type": media, "time_period": time_period, "rating": rating, "duration": duration});
    result = result.map((genre) => genre[0]);
    setGenres(result);
    setStep(1);
  }

  const finishStepOne = async (genre) => {
    let result = await pipeline(selections["country"], selections["type"], selections["time_period"], selections["rating"], selections["duration"], genre);
    setMedia(result);
    setStep(2);
  }

  const finishStepTwo = () => {
    setSelections(null);
    setGenres(null);
    setMedia(null);
    setStep(0);
  }

  const renderPage = () => {
    if (step === 0) return <SelectLabels handleSubmit={finishStepZero} />;
    if (step === 1) return <SelectGenre handleSubmit={finishStepOne} genres={genres} />;
    if (step === 2) return <SelectMedia media={media} handleSubmit={finishStepTwo} />
  }

  return <Container>
    <Stack direction="column" spacing={2} sx={{my:3}}>
      <Typography variant="h3">Netflix Automator</Typography>
      <MyStepper step={step} />
    </Stack>
    {renderPage()}
  </Container>
}

export default App;
