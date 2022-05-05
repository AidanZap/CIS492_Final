import * as React from 'react';
import {InputLabel, MenuItem, FormHelperText, FormControl, Select, Button } from "@mui/material";

export default function SelectLabels(props) {
  const [country, setCountry] = React.useState('');
  const [media, setMedia] = React.useState('');
  const [time_period, setTimePeriod] = React.useState('');
  const [rating, setRating] = React.useState('');
  const [duration, setDuration] = React.useState('');

  const handleChangeCountry = (event) => {
    setCountry(event.target.value);
  };

  const handleChangeMedia = (event) => {
    setMedia(event.target.value);
  };

  const handleChangeTimePeriod = (event) => {
    setTimePeriod(event.target.value);
  };

  const handleChangeRating = (event) => {
    setRating(event.target.value);
  };

  const handleChangeDuration = (event) => {
    setDuration(event.target.value);
  };

  return (
    <>
      <FormControl fullWidth>
        <InputLabel id="CountryLabel">Country</InputLabel>
        <Select
          labelId="CountryLabel"
          id="Country"
          value={country}
          label="Country"
          onChange={handleChangeCountry}
        >
          <MenuItem value={0}>All</MenuItem>
          <MenuItem value="United States">United States</MenuItem>
          <MenuItem value={"Other"}>Other</MenuItem>
        </Select>
        <FormHelperText>Please select desired region.</FormHelperText>
      </FormControl>
      
      <FormControl fullWidth>
        <InputLabel id="MediaLabel">Media</InputLabel>
        <Select
          labelId="MediaLabel"
          id="Media"
          value={media}
          label="Media"
          onChange={handleChangeMedia}
        >
          <MenuItem value={0}>All</MenuItem>
          <MenuItem value={1}>TV</MenuItem>
          <MenuItem value={2}>Movie</MenuItem>
        </Select>
        <FormHelperText>Please select desired media.</FormHelperText>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="TimePeriodLabel">Time Period</InputLabel>
        <Select
          labelId="TimePeriodLabel"
          id="TimePeriod"
          value={time_period}
          label="TimePeriod"
          onChange={handleChangeTimePeriod}
        >
          <MenuItem value={0}>All</MenuItem>
          <MenuItem value={1}>New</MenuItem>
          <MenuItem value={2}>2000's</MenuItem>
          <MenuItem value={3}>Pre-2000's</MenuItem>
        </Select>
        <FormHelperText>Please select desired time period.</FormHelperText>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="RatingLabel">Rating</InputLabel>
        <Select
          labelId="RatingLabel"
          id="Rating"
          value={rating}
          label="Rating"
          onChange={handleChangeRating}
        >
          <MenuItem value={1}>All</MenuItem>
          <MenuItem value={2}>Teenager Safe</MenuItem>
          <MenuItem value={3}>Kid Safe</MenuItem>
        </Select>
        <FormHelperText>Please select desired rating.</FormHelperText>
      </FormControl>

      <FormControl fullWidth>
        <InputLabel id="DurationLabel">Duration</InputLabel>
        <Select
          labelId="DurationLabel"
          id="Duration"
          value={duration}
          label="Duration"
          onChange={handleChangeDuration}
        >
          <MenuItem value={0}>All</MenuItem>
          <MenuItem value={1}>1-2 Seasons (TV)</MenuItem>
          <MenuItem value={2}>3+ Seasons (TV)</MenuItem>
          <MenuItem value={3}>Less than 90 Minutes (Movie)</MenuItem>
          <MenuItem value={4}>60-90 Minutes (Movie)</MenuItem>
          <MenuItem value={5}>90+ Minutes (Movie)</MenuItem>
        </Select>
        <FormHelperText>Please select desired duration.</FormHelperText>

        <Button onClick={() => {props.handleSubmit(country, media, time_period, rating, duration)}} variant="contained">Submit</Button>

      </FormControl>
    </>
  );
}