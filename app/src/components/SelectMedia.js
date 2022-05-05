import { Typography, Button, Stack, Pagination, Card, CardContent, Accordion, AccordionSummary, AccordionDetails, Grid } from "@mui/material";
import React from "react";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import HistoryIcon from '@mui/icons-material/History';

export default function SelectMedia(props) {

    const [page, setPage] = React.useState(0);

    return <>
        <Stack direction="column" spacing={1}>
            <Typography variant="h4">We found {props.media.length} titles you might be interested in</Typography>
            <Card>
                <CardContent>
                    <Grid container>
                        <Grid item xs={4}>
                            <Stack direction="column">
                                <Typography variant="h4" sx={{textDecoration: "underline"}}>{props.media[page].title === "" ? "N/A" : props.media[page].title}</Typography>
                                <Typography variant="h6">{props.media[page].release_year === "" ? "N/A" : props.media[page].release_year}</Typography>
                                <Typography variant="h6">{props.media[page].rating === "" ? "N/A" : props.media[page].rating}</Typography>
                                <Typography variant="h6">{props.media[page].duration === "" ? "N/A" : props.media[page].duration}</Typography>
                            </Stack>
                        </Grid>
                        <Grid item xs={8}>
                            <Stack direction="column">
                                <Accordion>
                                    <AccordionSummary expandIcon={<ExpandMoreIcon />} sx={{backgroundColor: "#1976d2"}}>
                                        <Typography variant="h6" color="white">Cast</Typography>
                                    </AccordionSummary>
                                    <AccordionDetails>
                                        <Typography>{String(props.media[page].cast).trim() === "" ? "N/A" : props.media[page].cast}</Typography>
                                    </AccordionDetails>
                                </Accordion>
                                <Accordion>
                                    <AccordionSummary expandIcon={<ExpandMoreIcon />} sx={{backgroundColor: "#1976d2"}}>
                                        <Typography variant="h6" color="white">Description</Typography>
                                    </AccordionSummary>
                                    <AccordionDetails>
                                        <Typography>{props.media[page].description === "" ? "N/A" : props.media[page].description}</Typography>
                                    </AccordionDetails>
                                </Accordion>
                                {props.media[page].keywords ? 
                                    <Accordion>
                                        <AccordionSummary expandIcon={<ExpandMoreIcon />} sx={{backgroundColor: "#1976d2"}}>
                                            <Typography variant="h6" color="white">Reviews are Saying [PREFETCHED FOR DEMO]</Typography>
                                        </AccordionSummary>
                                        <AccordionDetails>
                                            <Typography>{props.media[page].keywords}</Typography>
                                        </AccordionDetails>
                                    </Accordion> : <></>}
                            </Stack>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
            <Stack direction="row">
                <Pagination count={props.media.length} color="primary" onChange={(event, value) => { setPage(value -1) }}/>
                <Button variant="contained" color="error" onClick={props.handleSubmit}><HistoryIcon />Restart</Button>
            </Stack>
        </Stack>
    </>
}