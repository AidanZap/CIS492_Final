import { Grid, Button } from "@mui/material";

export default function SelectGenre(props) {

    return <Grid container justifyContent="center" alignItems="center" spacing={3}>
        {props.genres.map((genre, index) => {
            return <Grid key={index} item xs={3}>
                <Button variant="contained" size="large" onClick={() => {props.handleSubmit(genre)}}>{genre}</Button>
            </Grid>;
        })}
    </Grid>
}