import java.io.IOException;
import org.apache.hadoop.fs.Path; 
import org.apache.hadoop.io.*; 
import org.apache.hadoop.mapreduce.*; 
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat; 
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat; 
 
public class CharCount { 
 
    public sta c class CharMapper extends Mapper<LongWritable, Text, Text, IntWritable> { 
        private final sta c IntWritable one = new IntWritable(1); 
        private Text character = new Text(); 
 
        public void map(LongWritable key, Text value, Context context) throws IOExcep on, 
InterruptedExcep on { 
            String line = value.toString().toLowerCase().replaceAll("\\s+", ""); 
            for (char c : line.toCharArray()) { 
                if (Character.isLe er(c)) { 
                    character.set(Character.toString(c)); 
                    context.write(character, one); 
                } 
            } 
        } 
    } 
 
    public sta c class CharReducer extends Reducer<Text, IntWritable, Text, IntWritable> { 
        public void reduce(Text key, Iterable<IntWritable> values, Context context) 
                throws IOExcep on, InterruptedExcep on { 
            int sum = 0; 
            for (IntWritable val : values) 
                sum += val.get(); 
            context.write(key, new IntWritable(sum)); 
        } 
    } 
 
    public sta c void main(String[] args) throws Excep on { 
        Configura on conf = new Configura on(); 
        Job job = Job.getInstance(conf, "Character Count"); 
        job.setJarByClass(CharCount.class); 
        job.setMapperClass(CharMapper.class); 
        job.setReducerClass(CharReducer.class); 
        job.setOutputKeyClass(Text.class); 
        job.setOutputValueClass(IntWritable.class); 
        FileInputFormat.addInputPath(job, new Path(args[0])); 
        FileOutputFormat.setOutputPath(job, new Path(args[1])); 
        System.exit(job.waitForComple on(true) ? 0 : 1); 
    } 
} 