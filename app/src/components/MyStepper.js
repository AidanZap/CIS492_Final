import {Stepper, Step, StepLabel } from "@mui/material";

export default function MyStepper(props) {

    return <Stepper activeStep={props.step}>
        <Step>
            <StepLabel>General Questions</StepLabel>
        </Step>
        <Step>
            <StepLabel>Select Available Genre</StepLabel>
        </Step>
        <Step>
            <StepLabel>Decide on Media</StepLabel>
        </Step>
    </Stepper>
}