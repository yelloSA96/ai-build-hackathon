"use client";

import React, { useState, useEffect } from "react";
import { ChatProps } from "./chat";
import { Button } from "../ui/button";
import TextareaAutosize from "react-textarea-autosize";
import { PaperPlaneIcon, StopIcon } from "@radix-ui/react-icons";
import { v4 as uuidv4 } from "uuid";

// Assume Gamma is properly imported, adjust path as necessary
import Gamma from '../../lib/gamma';
import './styles.css'

import * as RadioGroup from '@radix-ui/react-radio-group';
import { Label } from "@radix-ui/react-label";
export default function ChatBottombar({
  messages,
  input,
  handleInputChange,
  handleSubmit,
  isLoading,
  error,
  stop,
  category
}: ChatProps ) {
  
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      console.log("coming to handleKeyDown")
      console.log(input)
      console.log(value)
      handleSubmit(e as unknown as React.FormEvent<HTMLFormElement>);
    }
  };


  const [result, setResult] = React.useState<{ category: string | null }>({
    category: null
  });
  const onSubmit = (data: { category: string }) => {
    setResult(data);
    console.log(data);
  };
  const [value, setValue] = React.useState("eastern_guru");
  return (
    <div className="p-4 flex justify-between w-full items-center gap-2">
      <form
        onSubmit={handleSubmit}
        className="w-full items-center flex relative gap-2"
      >
        <table className="w-full">
          <tr>
            <td>
        <TextareaAutosize
          autoComplete="off"
          value={input}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
          className="border-input max-h-10 px-5 py-4 text-sm shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 w-full border rounded-full flex items-center h-14 resize-none overflow-hidden dark:bg-card/35"
        />
        </td>
        <td>
        <Button
          variant="ghost"
          type="submit"
          size="icon"
          disabled={isLoading || !input.trim() || !value.trim()}
        >
          <PaperPlaneIcon />
        </Button>
        </td>
        </tr>
        <tr>
        <div  className="flex-column">
    <RadioGroup.Root className="RadioGroupRoot" defaultValue="eastern_guru" aria-label="View density"  onValueChange={setValue}>
      <div className='flex center'>
        <RadioGroup.Item className="RadioGroupItem" value="eastern_guru" id="r1">
          <RadioGroup.Indicator className="RadioGroupIndicator" />
        </RadioGroup.Item>
        <Label className="Label" >
        Eastern Guru
        </Label>
      </div>
      <div className='flex center'>
        <RadioGroup.Item className="RadioGroupItem" value=" toic_tutor" id="r2">
          <RadioGroup.Indicator className="RadioGroupIndicator" />
        </RadioGroup.Item>
        <label className="Label" htmlFor="r2">
        Stoic tutor
        </label>
      </div>
      <div className='flex center'>
        <RadioGroup.Item className="RadioGroupItem" value="existentialist" id="r3">
          <RadioGroup.Indicator className="RadioGroupIndicator" />
        </RadioGroup.Item>
        <label className="Label" htmlFor="r3">
        Existentialist
        </label>
      </div>
    </RadioGroup.Root>
    </div>
    </tr>
    </table>
      </form>
    </div>
  );
}


